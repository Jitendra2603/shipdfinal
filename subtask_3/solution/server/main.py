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
            # Encode the code as base64 to avoid issues with special characters
            encoded_code = base64.b64encode(code.encode()).decode()
            
            container = client.containers.run(
                image="python:3.8-slim",
                command=f"python -c \"import base64, sys; "
                        f"code = base64.b64decode('{encoded_code}').decode(); "
                        f"exec(code)\"",
                mem_limit="128m",
                memswap_limit="128m",
                cpu_quota=50000,  # Limit CPU usage to 50%
                network_disabled=True,
                detach=True,
                user="1000:1000",  # Run as non-root user
                security_opt=["no-new-privileges"],
                cap_drop=["ALL"],  # Drop all capabilities
                read_only=True,  # Make the container's root filesystem read-only    # Prevent privilege escalation
            )
    
            def timeout_handler(signum, frame):
                raise TimeoutError("Code execution timed out")
    
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(10)  # Set alarm for 10 seconds
    
            try:
                result = container.wait()
                stdout = container.logs(stdout=True, stderr=False).decode('utf-8').strip()
                stderr = container.logs(stdout=False, stderr=True).decode('utf-8').strip()
                
                if result['StatusCode'] == 0:
                    return CodeOutput(output=stdout, error=stderr, success=True)
                else:
                    return CodeOutput(output=stdout, error=stderr, success=False)
            except TimeoutError:
                return CodeOutput(error="Code execution timed out after 10 seconds.", success=False)
            finally:
                signal.alarm(0)  # Cancel the alarm
                try:
                    container.remove(force=True)
                except docker.errors.NotFound:
                    pass  # Container already removed
        except docker.errors.ContainerError as e:
            return CodeOutput(error=e.stderr.decode('utf-8'), success=False)
        except docker.errors.ImageNotFound:
            return CodeOutput(error="Docker image not found.", success=False)
        except docker.errors.APIError as e:
            return CodeOutput(error=f"Docker API error: {str(e)}", success=False)
        except Exception as e:
            return CodeOutput(error=f"Unexpected error: {str(e)}", success=False)


@app.post("/run_code", response_model=CodeResponse)
async def run_code(request: CodeRequest = Body(...)):
    return run_code_in_docker(request.code)
           
