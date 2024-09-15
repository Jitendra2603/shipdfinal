# Subtask 4: Save Submitted Code and Output to Database

Implement functionality to save the submitted code and its output to a database. The enhancements should include:

- **Database Model**: Create a `CodeSubmission` model to store code, output, and timestamps.
- **Database Connection**: Set up a connection to a PostgreSQL database using SQLAlchemy.
- **Submit Code Endpoint**: Add a `/submit_code` endpoint that executes the code and saves it to the database if successful.
- **Error Handling**: Ensure that failed code executions are not saved, and appropriate error messages are returned.

**Requirements**:

- Use SQLAlchemy ORM for database interactions.
- Protect against SQL injection and other common database vulnerabilities.
- Ensure that database sessions are properly managed and closed.
