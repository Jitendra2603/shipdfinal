# Subtask 3: Secure Code Execution Using Docker

Enhance the backend API to execute the code securely within a Docker container. This ensures that any malicious code does not affect the host system. The improvements should include:

- **Docker Integration**: Use Docker to create an isolated environment for code execution.
- **Resource Limitation**: Set constraints on CPU and memory usage for the container.
- **Security Measures**: Disable network access and run the container as a non-root user.
- **Error Handling**: Provide informative error messages if the container fails to execute.

**Requirements**:

- Use the Docker SDK for Python (`docker-py`) to manage containers.
- Update the `/run_code` endpoint to utilize Docker for code execution.
- Ensure that the solution is robust and handles potential Docker exceptions.
