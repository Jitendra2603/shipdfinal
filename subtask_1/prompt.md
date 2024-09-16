# Subtask 1: Frontend Code Editor

Your task is to implement a frontend code editor that allows users to write Python code. The editor should have the following features:

- **Syntax Highlighting**: Support for Python syntax highlighting using CodeMirror.
- **Code Input Area**: A text editor where users can write their Python code.
- **Run Code Button**: A button that sends the code to the backend API endpoint `/run_code` for execution.
- **Output Display**: An area where the output or error messages from the code execution are displayed.

**Requirements**:

- Use **React** as the JavaScript framework.
- Utilize **CodeMirror** (`@uiw/react-codemirror`) for the code editor with Python language mode.
- Implement the **Run Code** button to send a POST request to the `/run_code` endpoint with the following JSON payload:
  ```json
  {
    "code": "print('Hello, World!')"
  }
-  Display the response from the backend in the output area. The response will have the following structure:

```json
{
  "output": "Hello, World!\n",
  "error": "",
  "success": true
}
```
Ensure the UI is responsive and user-friendly.
Mock the backend API response initially to test the frontend implementation.
Endpoint Details:

Endpoint URL: http://127.0.0.1:8000/run_code
Method: POST
Headers: Content-Type: application/json
Payload:
```json
Copy code
{
  "code": "<user_code_here>"
}
```
Response:
```json
{
  "output": "<execution_output>",
  "error": "<error_messages>",
  "success": <boolean>
}
