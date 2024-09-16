import docker
from fastapi import FastAPI, Body, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, CodeSubmission
from schemas import CodeRequest, CodeResponse, SubmitCodeResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()
# Initialize Docker client with base_url from environment variable
docker_host = os.getenv('DOCKER_HOST', 'unix:///var/run/docker.sock')
client = docker.DockerClient(base_url=docker_host)

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

# Create all tables
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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
        error_message = e.stderr.decode('utf-8') if e.stderr else str(e)
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

@app.post("/submit_code", response_model=SubmitCodeResponse)
async def submit_code(request: CodeRequest = Body(...), db: Session = Depends(get_db)):
    result = run_code_in_docker(request.code)
    if result.success:
        try:
            submission = CodeSubmission(code=request.code, output=result.output)
            db.add(submission)
            db.commit()
            db.refresh(submission)
            return SubmitCodeResponse(code_output=result, db_success=True)
        except Exception as e:
            return SubmitCodeResponse(code_output=result, db_success=False, error=str(e))
    else:
        return SubmitCodeResponse(code_output=result, db_success=False, error="Code execution failed.")
