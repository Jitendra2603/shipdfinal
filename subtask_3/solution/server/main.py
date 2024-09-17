import docker
from fastapi import FastAPI, Body
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
client = docker.from_env()

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
        # Escape the code to handle special characters and multi-line inputs
        escaped_code = code.replace('"', '\\"').replace('\n', '\\n')
        result = client.containers.run(
            image="python:3.8-slim",
            command=f'python -c "{escaped_code}"',
            mem_limit="128m",
            cpu_quota=50000,  # Limit CPU usage to 50%
            network_disabled=True,
            stdout=True,
            stderr=True,
            user="1000:1000",  # Run as non-root user
            security_opt=["no-new-privileges"],  # Prevent privilege escalation
            remove=True  # Remove the container after execution
        )
        output = result.decode('utf-8')
        return CodeResponse(output=output, success=True)
    except docker.errors.ContainerError as e:
        error_message = e.stderr.decode('utf-8')
        return CodeResponse(error=error_message, success=False)
    except docker.errors.ImageNotFound:
        return CodeResponse(error="Docker image not found.", success=False)
    except docker.errors.APIError as e:
        return CodeResponse(error=f"Docker API error: {str(e)}", success=False)
    except Exception as e:
        return CodeResponse(error=f"Unexpected error: {str(e)}", success=False)

@app.post("/run_code", response_model=CodeResponse)
async def run_code(request: CodeRequest = Body(...)):
    return run_code_in_docker(request.code)
