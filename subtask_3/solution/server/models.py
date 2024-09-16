from sqlalchemy import Column, Integer, Text, DateTime, func
from database import Base

class CodeSubmission(Base):
    __tablename__ = "code_submissions"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(Text, nullable=False)
    output = Column(Text, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
