# Hints for Subtask 4

1. **Slight Hint**:
   - Define a SQLAlchemy `Base` model named `CodeSubmission` with fields for `id`, `code`, `output`, and `timestamp`. Use appropriate data types such as `Integer`, `Text`, and `DateTime`.
   - Example:
     ```python
     from sqlalchemy import Column, Integer, Text, DateTime, func
     from database import Base

     class CodeSubmission(Base):
         __tablename__ = "code_submissions"

         id = Column(Integer, primary_key=True, index=True)
         code = Column(Text, nullable=False)
         output = Column(Text, nullable=False)
         timestamp = Column(DateTime(timezone=True), server_default=func.now())
     ```

2. **Moderate Hint**:
   - Set up the database connection using SQLAlchemy. Create a `database.py` file that initializes the engine, session maker, and base declarative class. Use environment variables to manage sensitive information like the database URL.
   - Example:
     ```python
     from sqlalchemy import create_engine
     from sqlalchemy.ext.declarative import declarative_base
     from sqlalchemy.orm import sessionmaker
     import os

     DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost/postgres")

     engine = create_engine(DATABASE_URL)
     SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
     Base = declarative_base()
     ```

3. **Strong Hint**:
   - Implement the `/submit_code` endpoint to execute the code and, upon successful execution, save the code and its output to the database. Use dependency injection to manage database sessions within FastAPI. Ensure proper error handling to avoid saving failed executions.
   - Example:
     ```python
     from fastapi import Depends
     from sqlalchemy.orm import Session
     from database import SessionLocal
     from models import CodeSubmission

     def get_db():
         db = SessionLocal()
         try:
             yield db
         finally:
             db.close()

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
                 return SubmitCodeResponse(code_output=result, db_success=False, error=f"Failed to write to db: {e}")
         else:
             return SubmitCodeResponse(code_output=result, db_success=False)
     ```
   - Additionally, ensure that the frontend's "Submit Code" button correctly interacts with this endpoint and handles responses appropriately.
