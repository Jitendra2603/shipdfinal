---
Tests
---
Run the following commands:

```
docker-compose build
```
This will build the Docker images and install httpx and any other dependencies.

Once the containers are rebuilt, run the tests again using the following command:

```
docker-compose up
docker-compose run test
```
