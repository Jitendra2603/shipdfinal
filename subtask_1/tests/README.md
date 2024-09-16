Instructions to Run Tests for Subtask 1 in Docker
Now that we have the Docker configuration ready, here’s how you can run the tests easily inside a Docker container:

1. Build and Start the Frontend Service
This will start the frontend server.

```
docker-compose up frontend
```
You can access the frontend on http://localhost:3000.

2. Run the Frontend Tests
To run the tests inside a Docker container:

```
docker-compose run frontend-test
```
This will execute the tests specified in client/tests/CodeEditor.test.tsx using Jest.

3. Stop the Services
Once you're done, you can stop the Docker services with:

```
docker-compose down
```
