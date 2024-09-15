# Hints for Subtask 4

1. **Slight Hint**: Define a SQLAlchemy `Base` model for code submissions with fields for code, output, and timestamp.

2. **Moderate Hint**: Use dependency injection in FastAPI to manage database sessions.

3. **Strong Hint**: In the `/submit_code` endpoint, check if the code execution was successful before saving to the database.
