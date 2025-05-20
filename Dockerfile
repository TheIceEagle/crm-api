# Use an official Python runtime as a parent image
FROM python:3.13.3-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY ./requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the application code into the container at /app
# We copy the entire current directory context where Dockerfile is
COPY . /app

# Expose the port the app runs on (optional, as ports are mapped in docker-compose.yml)
EXPOSE 8000

# Command to run the application (can be overridden in docker-compose.yml)
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
# We've moved the command to docker-compose.yml for easier management