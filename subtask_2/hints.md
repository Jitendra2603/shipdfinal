# Hints for Subtask 2

1. **Slight Hint**:
   - Begin by setting up a basic FastAPI application. Install FastAPI and Uvicorn using pip, and create a simple `main.py` file with a root endpoint to verify the setup.

2. **Moderate Hint**:
   - Define a Pydantic model to parse the incoming JSON payload containing the Python code. Implement the `/run_code` POST endpoint that receives the code and prepares it for execution.
   - Example:
     ```python
     from fastapi import FastAPI, Body
     from pydantic import BaseModel

     class CodeRequest(BaseModel):
         code: str

     app = FastAPI()

     @app.post("/run_code")
     async def run_code(request: CodeRequest = Body(...)):
         # Code execution logic
     ```

3. **Strong Hint**:
   - Use the `asyncio` library to execute the received Python code asynchronously, preventing the server from blocking during execution. Implement proper error handling to catch and return any exceptions that occur during code execution.
   - Consider implementing a timeout mechanism to terminate long-running code executions.
   - Example:
     ```python
     import asyncio

     class CodeResponse(BaseModel):
         output: str = ""
         error: str = ""
         success: bool = False

     async def execute_code(code: str) -> CodeResponse:
         try:
             proc = await asyncio.create_subprocess_exec(
                 "python", "-c", code,
                 stdout=asyncio.subprocess.PIPE,
                 stderr=asyncio.subprocess.PIPE
             )
             stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=5)
             return CodeResponse(
                 output=stdout.decode(),
                 error=stderr.decode(),
                 success=proc.returncode == 0
             )
         except asyncio.TimeoutError:
             return CodeResponse(
                 error="TimeoutError: Code execution exceeded time limit.",
                 success=False
             )
         except Exception as e:
             return CodeResponse(
                 error=str(e),
                 success=False
             )

     @app.post("/run_code", response_model=CodeResponse)
     async def run_code(request: CodeRequest = Body(...)):
         return await execute_code(request.code)
     ```
