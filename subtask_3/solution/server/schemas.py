from pydantic import BaseModel

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
