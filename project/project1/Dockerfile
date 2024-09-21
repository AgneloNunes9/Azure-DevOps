# Use the official Python image as a base image
FROM python:3.8-slim

# Set environment variables for Flask
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define environment variable for version
ENV APP_VERSION=2.0.0

# Set the working directory in the container
WORKDIR /project1

# Install libreoffice and other dependencies
RUN apt-get update && \
    apt-get install -y libreoffice python3-uno unoconv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV PATH $PATH:/usr/lib/libreoffice/program

# Copy the requirements file into the container at /app
COPY requirements.txt /project1/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /project1/

# Expose port 5000
EXPOSE 5000

# Command to run the application using Gunicorn
CMD ["python", "main.py"]