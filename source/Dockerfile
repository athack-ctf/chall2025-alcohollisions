#########################################################################################################################
# TODO: REPLACE THE CONTENT OF THIS FILE WITH YOUR OWN.
#########################################################################################################################

# Use the official Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /chall

# Copy the requirements file and install dependencies
COPY src/requirements.txt .

RUN pip install -r requirements.txt

# Copy the application files into the container
COPY ./src .

# Expose port 5000 for Flask
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=challenge.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# Run the Flask app
CMD ["flask", "run"]
