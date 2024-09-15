---

The overall task is to create a secure web-based Python code runner that allows users to write, execute, and submit Python code through an interactive interface. The application comprises the following components:

- **Frontend**: A user-friendly code editor with syntax highlighting, where users can input Python code.
- **Backend API**: A server that receives code submissions, executes them securely in an isolated environment, and returns the output.
- **Secure Execution Environment**: Use Docker containers to execute code securely, preventing malicious code from affecting the host system.
- **Database**: Store submitted code and outputs for future reference and analysis.

Key considerations include:

- **Security**: Ensure that the code execution environment is isolated and cannot harm the host system.
- **Performance**: Optimize the application for fast response times and efficient resource usage.
- **Code Quality**: Write clean, maintainable code following best practices.

---

You will implement this project step-by-step through the following subtasks:

1. **Subtask 1**: Implement the frontend code editor.
2. **Subtask 2**: Develop the backend API for code execution.
3. **Subtask 3**: Enhance the backend to execute code securely using Docker.
4. **Subtask 4**: Implement database functionality to save submitted code and outputs.
