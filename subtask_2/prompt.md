Subtask 2: Backend Code Execution API
---
Implement a backend API that accepts Python code from the frontend, executes it, and returns the output. The API should:

Endpoint: Provide a /run_code POST endpoint that accepts a JSON payload containing the code.

Payload Structure:

```
{
  "code": "print('Hello, World!')"
}
```
Code Execution: Execute the received Python code securely on the server.

Response: Return a JSON response with the following keys:

"output": The standard output from the code execution.
"error": Any error messages produced during code execution.
"success": A boolean indicating whether the code executed successfully.
Example Response:

```
{
  "output": "Hello, World!\n",
  "error": "",
  "success": true
}
```
Error Handling: Gracefully handle any exceptions or errors in code execution, and include error messages in the "error" field.

Timeout Mechanism: Implement a timeout to prevent long-running code from hanging the server. If the execution exceeds the time limit (e.g., 5 seconds), terminate it and return an appropriate error message.

Requirements:

Use FastAPI for the backend implementation.
Ensure that the API is asynchronous to handle multiple requests efficiently.
Avoid blocking the server during code execution.
Configure CORS settings to allow requests from the frontend (e.g., http://localhost:3000).
Update the frontend to make actual API calls to the backend.
Additional Notes:

The endpoint name and payload structure should match exactly what the frontend is expecting, as defined in Subtask 1.
Include all necessary files and configurations to run the backend independently at this stage like uvicorn config, requirements, etc. in the server folder
