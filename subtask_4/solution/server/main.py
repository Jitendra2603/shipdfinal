import subprocess
import sys
from typing import Union

from database import SessionLocal
from fastapi import Body, Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from schemas import CodeResult
from sqlalchemy.orm import Session
import docker

app = FastAPI()


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

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class CodeRequest(BaseModel):
    code: str

class CodeOutput(BaseModel):
    output: str = ""
    error: str = ""
    success: bool = False

@app.post("/run_code")
async def run_code(request: CodeRequest = Body()):
    return _run_code(request.code)

class SubmitCodeResponse(BaseModel):
    code_output: CodeOutput
    db_success: bool
    error: Union[str, None] = None

@app.post("/submit_code")
async def submit_code(request: CodeRequest = Body(), db: Session = Depends(get_db)):
    result = _run_code(request.code)
    if result.success:
        try:
            create_code_result(code_result=CodeResult(code=request.code, output=result.output), db=db)
            return SubmitCodeResponse(code_output=result, db_success=True)
        except Exception as e:
            return SubmitCodeResponse(code_output=result, db_success=False, error=f"Failed to write to db: {e}")
    else:
        return SubmitCodeResponse(code_output=result, db_success=False)

def _run_code(code):
    try:
        client = docker.from_env()
        # Escape the code to handle special characters and multi-line inputs
        escaped_code = code.replace('"', '\\"').replace('\n', '\\n')
        print(escaped_code)
        try:
            container = client.containers.run(
                "python:3.8-slim",
                f'python -c "{escaped_code}"',
                detach=True,
                mem_limit="128m",
                cpu_period=100000,
                cpu_quota=50000,
                network_disabled=True,
                stdout=True,
                stderr=True,
                remove=False,  # Do not remove the container immediately
                user="1000:1000",  # Run as non-root user
                security_opt=["no-new-privileges"]  # Prevent privilege escalation
            )
            
            result = container.wait()  # Ensure the container has finished executing
            logs = container.logs(stdout=True, stderr=True)
            
            stdout, stderr = logs.split(b'\n', 1) if b'\n' in logs else (logs, b'')
            container.remove()  # Remove the container after fetching logs
            return CodeOutput(
                output=stdout.decode('utf-8').strip(),
                error=stderr.decode('utf-8').strip(),
                success=result['StatusCode'] == 0
            )
        except docker.errors.ImageNotFound:
            return CodeOutput(
                error="Docker image not found. Please ensure the image 'python:3.8-slim' is available."
            )
        except docker.errors.ContainerError as e:
            return CodeOutput(
                error=f"Container error: {str(e)}"
            )
        except docker.errors.APIError as e:
            return CodeOutput(
                error=f"Docker API error: {str(e)}"
            )
    except Exception as e:
        return CodeOutput(
            error=f"Unexpected error: {str(e)}"
        )

def create_code_result(code_result: CodeResult, db: Session):
    db_item = CodeResult(code=code_result.code, output=code_result.output)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
