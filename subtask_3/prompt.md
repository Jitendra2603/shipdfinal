# Subtask 3: Secure Code Execution Using Docker

Enhance the backend API to execute the code securely within a Docker container. This ensures that any malicious code does not affect the host system. The improvements should include:

Docker Integration: Use Docker to create an isolated environment for code execution.
Resource Limitation: Set constraints on CPU and memory usage for the container.
Security Measures: Disable network access and run the container as a non-root user.
Error Handling: Provide informative error messages if the container fails to execute.
Specifications:

API Endpoint: The /run_code POST endpoint remains the same as in Subtask 2.

Payload Structure: The request body should be a JSON object with a "code" key containing the code as a string.

Example payload:

```
{
  "code": "print('Hello, World!')"
}
```
Response Structure: The response should have the same structure as in Subtask 2.

Example response:

```
{
  "output": "Hello, World!\n",
  "error": "",
  "success": true
}
```
Requirements:

Use the Docker SDK for Python (docker-py) to manage containers.
Update the /run_code endpoint to utilize Docker for code execution.
Ensure that the solution is robust and handles potential Docker exceptions.
Configure CORS settings to allow requests from the frontend (e.g., http://localhost:3000).
Update the frontend if necessary to handle any changes.
Additional Notes:

The code execution should happen inside a Docker container with limited resources.

The Docker container should:

Use a lightweight Python image, such as python:3.8-slim.
Limit memory usage (e.g., 128MB).
Limit CPU usage (e.g., 50% of a CPU).
Disable network access.
Run as a non-root user.
Prevent privilege escalation.
Include all necessary files and configurations to run both the backend and frontend independently at this stage.

Ensure that the entire repository up to this point is included, including any media files.
