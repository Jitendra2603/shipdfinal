#!/bin/bash

echo "Running HTTP Test..."

# Wait for the Docker container to be ready
echo "Waiting for the application to start..."
sleep 10  # Adjust the sleep time if necessary

# Send a request to the application
HTTP_RESPONSE=$(curl --write-out "%{http_code}" --silent --output /dev/null http://localhost:3000)

if [ "$HTTP_RESPONSE" -eq 200 ]; then
    echo "Test Passed: Application is accessible at http://localhost:3000"
else
    echo "Test Failed: Application is not accessible. HTTP Status Code: $HTTP_RESPONSE"
    exit 1
fi

echo "HTTP Test passed successfully."
