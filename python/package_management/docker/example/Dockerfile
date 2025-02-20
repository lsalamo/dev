# syntax=docker/dockerfile:1
# Use the official Python image from the Docker Hub
# image: pythom + tag: 3.9-slim (https://hub.docker.com/_/python)
FROM python:3.14.0a1-slim
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
# Copy files code into the container
COPY . .
# Run the Flask app
# CMD [ "python", "./your-daemon-or-script.py" ]
CMD ["flask", "run", "--debug"]
