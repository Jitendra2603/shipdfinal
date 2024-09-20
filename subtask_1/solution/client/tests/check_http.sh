#!/bin/bash

echo "Running HTTP Test..."

# Function to check if the application is ready
check_app_ready() {
    local max_attempts=30
    local wait_seconds=2
    local attempt=1
    local url="http://localhost:3000"

    echo "Waiting for the application to start..."

    while [ $attempt -le $max_attempts ]; do
        HTTP_RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" $url)
        if [ "$HTTP_RESPONSE" -eq 200 ]; then
            echo "Application is ready after $((attempt * wait_seconds)) seconds."
            return 0
        fi
        echo "Attempt $attempt: Application not ready yet. Waiting $wait_seconds seconds..."
        sleep $wait_seconds
        attempt=$((attempt + 1))
    done

    echo "Application failed to start after $((max_attempts * wait_seconds)) seconds."
    return 1
}

# Check if the application is ready
if check_app_ready; then
    echo "Test Passed: Application is accessible at http://localhost:3000"
else
    echo "Test Failed: Application is not accessible within the timeout period."
    exit 1
fi

# Additional checks for application content
CONTENT=$(curl -s http://localhost:3000)

if echo "$CONTENT" | grep -q "Datacurve"; then
    echo "Test Passed: Application content verified."
else
    echo "Test Failed: Expected content not found on the page."
    exit 1
fi

echo "HTTP Test passed successfully."
