Navigate to the subtask_3 Directory

Open your terminal or command prompt and navigate to the subtask_3 directory:

```
cd C:\shipdfinal\subtask_3
```
Ensure Docker Daemon is Listening on TCP Port 2375

Verify that Docker is listening on tcp://localhost:2375:
```
docker -H tcp://localhost:2375 version
```
You should see version information without errors.

Build the Docker Images

Run the following command to build the Docker images for all services (web, db, and test):

```
docker-compose build
```
Expected Output:

Successful build of web and test services without errors related to missing paths.
Run the Tests

Execute the tests by bringing up the test service:
```
docker-compose up test
```
