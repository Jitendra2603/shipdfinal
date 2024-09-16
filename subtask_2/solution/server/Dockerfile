# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install the testing dependencies
RUN pip install pytest fastapi[testclient]

# Expose the port for FastAPI
EXPOSE 8000

# Command to run the tests
CMD ["pytest", "test_main.py"]
