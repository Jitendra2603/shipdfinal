```
git clone https://github.com/Jitendra2603/shipdfinal.git
```
```
cd shipdfinal/subtask_1
```

Make the test script executable:

```
chmod +x tests/test.sh
```
Run the test script:
```
./tests/test.sh
```
or 
```
sh tests/test.sh
```
> [!Note]
> On windows, you can directly run the above command on Git bash

Navigate to the subtask_1/solution/client directory:

```
cd subtask_1/solution/client
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
or 
```
sh tests/test.sh
```
> [!Note]
> On Windows, you can directly run the above command in Git Bash
