#!/bin/bash

echo "Running Subtask 1 Tests..."

# Print the current working directory
echo "Current Directory: $(pwd)"

# Function to find a file and check if it exists
find_and_check_file() {
    local file_name=$1
    local search_path=$2
    local file_path=$(find "$search_path" -name "$file_name" -print -quit 2>/dev/null)
    
    if [ -n "$file_path" ]; then
        echo "Test Passed: File '$file_name' exists at $file_path"
        return 0
    else
        echo "Test Failed: File '$file_name' does not exist in $search_path"
        return 1
    fi
}

# Check for video file
find_and_check_file "wave-loop.mp4" ".." || exit 1

# Check for favicon
find_and_check_file "favicon.ico" ".." || exit 1

# Check for CodeEditor component
find_and_check_file "CodeEditor.tsx" ".." || exit 1

# Find the client directory
CLIENT_DIR=$(find ".." -type d -name "client" -print -quit)

if [ -z "$CLIENT_DIR" ]; then
    echo "Test Failed: Could not find the client directory"
    exit 1
fi

# Check if the application builds successfully
echo "Building the application..."
cd "$CLIENT_DIR" || exit 1

npm install

if npm run build; then
    echo "Test Passed: Application builds successfully."
else
    echo "Test Failed: Application failed to build."
    exit 1
fi

echo "All tests passed successfully."
