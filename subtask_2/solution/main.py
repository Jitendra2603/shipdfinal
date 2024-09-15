import asyncio
from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class CodeRequest(BaseModel):
    code: str

class CodeResponse(BaseModel):
    output: str = ""
    error: str = ""
    success: bool = False

async def run_user_code(code: str) -> CodeResponse:
    try:
        proc = await asyncio.create_subprocess_exec(
            "python", "-c", code,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        try:
            stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=5)
        except asyncio.TimeoutError:
            proc.kill()
            await proc.communicate()
            return CodeResponse(error="TimeoutError: Code execution exceeded time limit.", success=False)

        output = stdout.decode()
        error = stderr.decode()
        success = proc.returncode == 0
        return CodeResponse(output=output, error=error, success=success)
    except Exception as e:
        return CodeResponse(error=str(e), success=False)

@app.post("/run_code", response_model=CodeResponse)
async def run_code(request: CodeRequest = Body(...)):
    return await run_user_code(request.code)
