# Subtask 2: Backend Code Execution API

Implement a backend API that accepts Python code from the frontend, executes it, and returns the output. The API should:

- **Endpoint**: Provide a `/run_code` POST endpoint that accepts a JSON payload containing the code.
- **Code Execution**: Execute the received Python code securely.
- **Response**: Return a JSON response with the code's output, any error messages, and a success flag.
- **Error Handling**: Gracefully handle any exceptions or errors in code execution.

**Requirements**:

- Use a modern Python web framework like **FastAPI**.
- Ensure that the API is asynchronous to handle multiple requests efficiently.
- Avoid blocking the server during code execution.
