Navigate to the tests/ directory.

Install the required testing dependencies (e.g., pytest, requests).

```
pip install pytest requests
```
Run the tests:

```
python -m unittest test_main.py
```
The tests will send requests to http://localhost:8000 and verify the responses.

Notes:
Docker-in-Docker: To run Docker inside a Docker container (which is necessary for the backend to run code inside Docker containers), we mount the Docker socket from the host machine into the backend container:

```
volumes:
  - /var/run/docker.sock:/var/run/docker.sock
