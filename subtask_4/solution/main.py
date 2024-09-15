import docker
from fastapi import FastAPI, Body, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, CodeSubmission

app = FastAPI()
client = docker.from_env()
Base.metadata.create_all(bind=engine)

class CodeRequest(BaseModel):
    code: str

class CodeResponse(BaseModel):
    output: str = ""
    error: str = ""
    success: bool = False

class SubmitCodeResponse(BaseModel):
    code_output: CodeResponse
    db_success: bool
    error: str = ""

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def run_code_in_docker(code: str) -> CodeResponse:
    try:
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

@app.post("/submit_code", response_model=SubmitCodeResponse)
async def submit_code(request: CodeRequest = Body(...), db: Session = Depends(get_db)):
    result = run_code_in_docker(request.code)
    if result.success:
        submission = CodeSubmission(code=request.code, output=result.output)
        db.add(submission)
        db.commit()
        db.refresh(submission)
        return SubmitCodeResponse(code_output=result, db_success=True)
    else:
        return SubmitCodeResponse(code_output=result, db_success=False, error="Code execution failed.")
