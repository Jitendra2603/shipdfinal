Make the test script executable:

```
chmod +x tests/test.sh
```
Run the test script:
```
./tests/test.sh
```
Navigate to the subtask_1/solution directory:

```
cd subtask_1/solution
```
Build the Docker image using Docker Compose:

```
docker-compose build
```
Run the Docker container:

```
docker-compose up
```
The frontend application should now be accessible at http://localhost:3000
Ensure the Docker container is running:

```
docker-compose up -d
```
Make the HTTP test script executable:

```
chmod +x tests/check_http.sh
```
Run the HTTP test script:

```
./tests/check_http.sh
```
