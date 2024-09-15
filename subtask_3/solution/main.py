import docker
from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()
client = docker.from_env()

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
            image="python:3.9-slim",
            command=f'python -c "{escaped_code}"',
            mem_limit="128m",
            cpu_quota=50000,
            network_disabled=True,
            stdout=True,
            stderr=True,
            user="nobody",
            security_opt=["no-new-privileges"],
            remove=True
        )
        output = result.decode('utf-8')
        return CodeResponse(output=output, success=True)
    except docker.errors.ContainerError as e:
        error_message = e.stderr.decode('utf-8')
        return CodeResponse(error=error_message, success=False)
    except Exception as e:
        return CodeResponse(error=str(e), success=False)

@app.post("/run_code", response_model=CodeResponse)
async def run_code(request: CodeRequest = Body(...)):
    return run_code_in_docker(request.code)
