Navigate to the subtask_3 Directory

Open your terminal or command prompt and navigate to the subtask_3 directory:

```
cd C:\shipdfinal\subtask_3
```
![Note]
> Only for Windows
Ensure Docker Daemon is Listening on TCP Port 2375

Verify that Docker is listening on tcp://localhost:2375:
```
docker -H tcp://localhost:2375 version
```
You should see version information without errors.

Build the Docker Images

Run the following command to build the Docker images for all services (web and backend):

```
docker-compose build
```
Expected Output:

Successful build of web and test services without errors related to missing paths.
Execute the tests by bringing up the test service:
```
docker-compose up
```
Run the Tests:
```
pip install unittest
```
```
cd tests
```
```
python -m unittest test_main.py
```
The tests will send requests to http://localhost:8000 and verify the responses.

![Caution]
>Docker-in-Docker: To run Docker inside a Docker container (which is necessary for the backend to run code inside Docker containers), we mount the Docker socket from the host machine into the backend container:

```
volumes:
  - /var/run/docker.sock:/var/run/docker.sock



