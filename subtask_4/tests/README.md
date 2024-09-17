Option 1: Using docker-compose exec

After starting the services with docker-compose up --build, execute the tests inside the backend container.

```
docker-compose exec web bash
```
Inside the container, run:

```
pytest tests/test_main.py
```
Option 2: Using a Separate Test Service

Alternatively, you can define a separate service in docker-compose.yml for running tests. This approach isolates the test execution from the running backend service.

Update docker-compose.yml

```yaml
version: '3.8'

services:
  web:
    build: ./server
    ports:
      - "8000:80"
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgresql://postgres:password@db/postgres
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock  # Needed to run Docker inside Docker

  db:
    image: postgres:13
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
      POSTGRES_DB: postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data

  tests:
    build: ./server
    command: ["pytest", "tests/test_main.py"]
    depends_on:
      - web
      - db
    environment:
      - DATABASE_URL=postgresql://postgres:password@db/postgres

volumes:
  postgres_data:

```
Execute the tests using the tests service:

```
docker-compose run tests
```
This command will build the backend image if necessary and run the tests defined in tests/test_main.py.

Ensure Database is Ready Before Running Tests

Sometimes, tests might run before the database is fully ready. To handle this, you can use a wait-for-it script or similar to delay the start of the test service until the database is ready.

Example Using wait-for-it.sh

Download wait-for-it.sh

Place the wait-for-it.sh script in the server/ directory.

Modify Dockerfile

```
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Install test dependencies
RUN pip install pytest

# Copy wait-for-it script
COPY wait-for-it.sh /code/wait-for-it.sh
RUN chmod +x /code/wait-for-it.sh

# Copy project
COPY . /code/

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
```
Modify docker-compose.yml

```yaml
version: '3.8'

services:
  web:
    build: ./server
    ports:
      - "8000:80"
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgresql://postgres:password@db/postgres
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock  # Needed to run Docker inside Docker

  db:
    image: postgres:13
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
      POSTGRES_DB: postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data

  tests:
    build: ./server
    command: ["./wait-for-it.sh", "db:5432", "--", "pytest", "tests/test_main.py"]
    depends_on:
      - web
      - db
    environment:
      - DATABASE_URL=postgresql://postgres:password@db/postgres

volumes:
  postgres_data:
```
This setup ensures that the tests service waits for the PostgreSQL database to be ready before executing the tests.
