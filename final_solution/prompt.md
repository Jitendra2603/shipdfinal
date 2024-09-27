# Subtask 4: Save Submitted Code and Output to Database and CSS

Implement functionality to save the submitted code and its output to a database. The enhancements should include:

Database Model: Create a CodeSubmission model to store code, output, and timestamps.
Database Connection: Set up a connection to a PostgreSQL database using SQLAlchemy.
Submit Code Endpoint: Add a /submit_code POST endpoint that executes the code and saves it to the database if successful.
Error Handling: Ensure that failed code executions are not saved, and appropriate error messages are returned.
Specifications:

API Endpoint: Provide a /submit_code POST endpoint.

Payload Structure: The request body should be a JSON object with a "code" key containing the code as a string.

Example payload:

```
{
  "code": "print('Hello, World!')"
}
```
Response Structure: The response should include the execution result and whether the database save was successful.

Example response:

```
{
  "code_output": {
    "output": "Hello, World!\n",
    "error": "",
    "success": true
  },
  "db_success": true,
  "error": ""
}
```
Database: Use PostgreSQL as the database. The connection string should be configurable via environment variables or a .env file.

Requirements:

Use SQLAlchemy ORM for database interactions.
Protect against SQL injection and other common database vulnerabilities.
Ensure that database sessions are properly managed and closed.
Configure CORS settings to allow requests from the frontend (e.g., http://localhost:3000).
Update the frontend to add a "Submit Code" button that sends a request to the /submit_code endpoint.
Include all necessary files and configurations to run both the backend and frontend independently at this stage.
Ensure that the entire repository up to this point is included, including any media files.
Additional Notes:

The code should only be saved to the database if the code execution was successful (success: true).
If the code execution fails, return appropriate error messages and do not save the submission to the database.
Update the frontend to handle the new endpoint and provide user feedback.

Add CSS using globals.css file and layout.tsx file.
