# Hints for Subtask 2
---
Slight Hint: Set up a basic FastAPI application with the required /run_code endpoint.

Moderate Hint: Use the subprocess module to execute the code in a separate process and capture stdout and stderr.

Strong Hint: Use asyncio.create_subprocess_exec to run the code asynchronously, and implement a timeout using asyncio.wait_for to prevent long-running executions.
