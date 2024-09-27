---
Tests
---
```
git clone https://github.com/Jitendra2603/shipdfinal.git
```
```
cd shipdfinal/subtask_2
```
Run the following commands:

```
docker-compose build
```
This will build the Docker images and install httpx and any other dependencies.

Once the containers are rebuilt, run:

```
docker-compose up
```
---
# Tests

```
python -m unittest tests/test_main.py
```
or
```
python -m pytest tests/test_main.py
```
