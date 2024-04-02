# Use the official Ubuntu base image
FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /app

# Update package lists and install any required dependencies
RUN apt-get update && \
    apt-get install -y \
    # Add your required packages here, for example:
    python3 \
    python3-pip

# Copy the local project directory to the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose port 8000 to allow communication to/from server
EXPOSE 8000

# Run Django's built-in development server when the container launches
CMD ["python3", "manage.py", "runserver", "127.0.0.1:8000"]
