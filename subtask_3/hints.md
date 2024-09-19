# Hints for Subtask 3

1. **Slight Hint**:
   - Install the Docker SDK for Python by adding `docker` to your `requirements.txt` and installing it using `pip install docker`. Ensure that Docker is running on your system.

2. **Moderate Hint**:
   - Modify the code execution function to utilize Docker containers. Use the `docker.from_env()` method to initialize the Docker client. Configure the container to run the Python code with resource limitations such as memory and CPU quotas.
   - Example:
     ```python
     import docker

     client = docker.from_env()

     def run_code_in_docker(code: str) -> CodeResponse:
         try:
             container = client.containers.run(
                 image="python:3.9-slim",
                 command=f'python -c "{code}"',
                 mem_limit="128m",
                 cpu_quota=50000,
                 network_disabled=True,
                 stdout=True,
                 stderr=True,
                 user="nobody",
                 security_opt=["no-new-privileges"],
                 remove=True
             )
             output = container.decode('utf-8')
             return CodeResponse(output=output, success=True)
         except docker.errors.ContainerError as e:
             return CodeResponse(error=e.stderr.decode('utf-8'), success=False)
         except docker.errors.ImageNotFound:
             return CodeResponse(error="Docker image not found.", success=False)
         except docker.errors.APIError as e:
             return CodeResponse(error=str(e), success=False)
     ```

3. **Strong Hint**:
   - Enhance security by disabling network access within the Docker container and running the container as a non-root user. Handle specific Docker exceptions to provide clear error messages. Ensure that the container is removed after execution to prevent resource leaks.
   - Implement additional security measures such as setting `security_opt=["no-new-privileges"]` and limiting the container's capabilities.
   - Example:
     ```python
     def run_code_in_docker(code: str) -> CodeResponse:
         try:
             escaped_code = code.replace('"', '\\"').replace('\n', '\\n')
             result = client.containers.run(
                 image="python:3.9-slim",
                 command=f'python -c "{escaped_code}"',
                 mem_limit="128m",
                 cpu_quota=50000,
                 network_disabled=True,
                 stdout=True,
                 stderr=True,
                 user="nobody",
                 security_opt=["no-new-privileges"],
                 remove=True
             )
             output = result.decode('utf-8')
             return CodeResponse(output=output, success=True)
         except docker.errors.ContainerError as e:
             error_message = e.stderr.decode('utf-8') if e.stderr else "Container execution failed."
             return CodeResponse(error=error_message, success=False)
         except docker.errors.ImageNotFound:
             return CodeResponse(
                 error="Docker image not found. Please ensure the image 'python:3.9-slim' is available.",
                 success=False
             )
         except docker.errors.APIError as e:
             return CodeResponse(
                 error=f"Docker API error: {str(e)}",
                 success=False
             )
         except Exception as e:
             return CodeResponse(error=str(e), success=False)
     ```
