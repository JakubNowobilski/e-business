# Use an official Node.js runtime as a parent image
FROM node:20

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# If you are building your code for production
# RUN npm ci --only=production

# Copy the rest of the application code to the working directory
COPY ./src ./src
COPY ./resources ./resources

# Expose the port the app runs on
EXPOSE 8080

# Define the command to run the app
CMD [ "node", "src/server.js" ]
