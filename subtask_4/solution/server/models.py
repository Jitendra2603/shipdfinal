from sqlalchemy import Column, Integer, String
from .database import Base

class CodeResult(Base):
    __tablename__ = "code_result"
    id = Column(Integer, primary_key=True)
    code = Column(String)
    output = Column(String)
