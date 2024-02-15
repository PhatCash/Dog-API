# Base Image
FROM python:alpine

# Specify the maintainer of the container image
LABEL maintainer="vicastro@pdx.edu"

# Copy the contents of the current directory into the container directory /app
COPY . /app

# Set the working directory of the container to /app
WORKDIR /app

# Install the Python packages 
RUN pip install -r requirements.txt

# Set parameters using Gunicorn server 
CMD gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 app:app
