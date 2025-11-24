# Dockerfile

# Use a minimal Python image as the base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application file into the container
COPY app.py /app/

# The ENV instruction sets an environment variable inside the image.
# We will pass the tag from Jenkins during the build process.
ARG IMAGE_TAG
ENV IMAGE_TAG=${IMAGE_TAG}

# Command to run the application when the container starts
CMD ["python", "app.py"]
