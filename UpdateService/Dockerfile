# Use an official Python runtime as a parent image
FROM ubuntu

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Specify the version of pip directly
RUN apt -y update
RUN apt -y install python3-pip

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
# EXPOSE 80

# Define environment variable
# ENV NAME World

# Run app.py when the container launches
CMD ["python3", "github_data_api.py"]