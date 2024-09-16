Action Steps:

Navigate to Project Root:

```
cd subtask_1
Build the Test Docker Image:

```
```
docker build -f solution/client/Dockerfile.test -t frontend-tests solution/client
```
Run the Tests:

```
docker run frontend-tests
```
Expected Output:

```
  CodeEditor Component
    ✓ renders without crashing
    ✓ syntax highlighting works
    ✓ run code button triggers code execution and displays output
    ✓ submit code button triggers code submission and displays output

  4 passing (2s)
```
