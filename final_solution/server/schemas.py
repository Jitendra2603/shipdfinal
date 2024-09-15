from pydantic import BaseModel

class CodeResult(BaseModel):
    code: str
    output: str
