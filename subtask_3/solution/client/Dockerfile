# Use an official Node.js runtime as a parent image
FROM node:16-alpine

# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the application code
COPY . /app

# Expose port 3000
EXPOSE 3000

# Run the application
CMD ["npm", "run", "dev"]
