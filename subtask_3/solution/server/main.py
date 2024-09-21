import docker
from fastapi import FastAPI, Body
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os
import tempfile

app = FastAPI()
if os.name == 'nt':  # Windows
    client = docker.DockerClient(base_url='tcp://localhost:2375')
else:  # Unix-based systems
    client = docker.DockerClient(base_url='unix:///var/run/docker.sock')

# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeRequest(BaseModel):
    code: str

class CodeResponse(BaseModel):
    output: str = ""
    error: str = ""
    success: bool = False

def run_code_in_docker(code: str) -> CodeResponse:
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as temp_file:
            temp_file.write(code)
            temp_file_path = temp_file.name

        container = client.containers.run(
            image="python:3.8-slim",
            command=f"python {os.path.basename(temp_file_path)}",
            volumes={os.path.dirname(temp_file_path): {'bind': '/code', 'mode': 'ro'}},
            working_dir="/code",
            mem_limit="128m",
            cpu_quota=50000,  # Limit CPU usage to 50%
            network_disabled=True,
            detach=True,
            stdout=True,
            stderr=True,
            user="1000:1000",  # Run as non-root user
            security_opt=["no-new-privileges"],  # Prevent privilege escalation
        )

        try:
            container.wait(timeout=10)  # Wait for the container to finish with a 10-second timeout
            output = container.logs().decode('utf-8')
            return CodeResponse(output=output, success=True)
        except docker.errors.NotFound:
            return CodeResponse(error="Container was terminated due to resource constraints or timeout.", success=False)
        finally:
            try:
                container.remove(force=True)
            except docker.errors.NotFound:
                pass  # Container already removed
            os.unlink(temp_file_path)  # Remove the temporary file

    except docker.errors.ContainerError as e:
        return CodeResponse(error=e.stderr.decode('utf-8'), success=False)
    except docker.errors.ImageNotFound:
        return CodeResponse(error="Docker image not found.", success=False)
    except docker.errors.APIError as e:
        return CodeResponse(error=f"Docker API error: {str(e)}", success=False)
    except Exception as e:
        return CodeResponse(error=f"Unexpected error: {str(e)}", success=False)

@app.post("/run_code", response_model=CodeResponse)
async def run_code(request: CodeRequest = Body(...)):
    return run_code_in_docker(request.code)
           
