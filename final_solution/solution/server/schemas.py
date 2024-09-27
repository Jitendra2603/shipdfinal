from pydantic import BaseModel

class CodeResultSchema(BaseModel):
    id: int
    code: str
    output: str

    class Config:
        orm_mode = True
