
# Subtask 1: Frontend Code Editor

Your task is to implement a frontend code editor that allows users to write Python code. The editor should have the following features:

### Features:

1. **Syntax Highlighting**: Support for Python syntax highlighting.
2. **Code Input Area**: A text editor where users can write their Python code.
3. **Run Code Button**: A button that sends the code to the backend API for execution.
4. **Output Display**: An area where the output or error messages from the code execution are displayed.

---

### Specifications:

- **API Endpoint**: When the "Run Code" button is clicked, the editor should send a POST request to the backend API endpoint `/run_code`.
  
- **Payload Structure**: The POST request should have a JSON body with a single key `"code"` containing the code as a string.

#### Example payload:

```json
{
  "code": "print('Hello, World!')"
}
```

- **Response Handling**: The frontend should handle the response from the backend, which will be a JSON object containing the keys `"output"`, `"error"`, and `"success"`. Display the `"output"` or `"error"` in the output display area accordingly.

#### Example backend response:

```json
{
  "output": "Hello, World!\n",
  "error": "",
  "success": true
}
```

---

### Requirements:

- **Use React and Next.js** for the frontend implementation.
- Ensure the **UI is responsive** and user-friendly.
- Handle user inputs and outputs gracefully, providing feedback where necessary.
- Since the backend is not yet implemented, you can **mock the API response** in your frontend code to simulate the interaction.

---

### Notes:

- Prepare your frontend code to be ready to integrate with the backend API in the next subtasks.
- Include all necessary files and assets so that the application can run independently at this stage.
