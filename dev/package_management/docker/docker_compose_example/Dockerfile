# syntax=docker/dockerfile:1
# Use the official Python image from the Docker Hub
FROM python:3.9-slim
# Set the working directory in the container
WORKDIR /app
# envrionment variables
ENV FLASK_APP=app/app.py
ENV FLASK_RUN_HOST=0.0.0.0
# Copy the requirements file into the container
COPY requirements.txt requirements.txt
# Install the dependencies
RUN pip install -r requirements.txt
# Expose port 5000 for the Flask app
EXPOSE 5000
COPY . . 
# Run the Flask app
CMD ["flask", "run", "--debug"]