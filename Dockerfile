# Use a base image with Python 3.9
FROM python:3.13-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the Flask port
EXPOSE 5000

# Run the application
CMD ["python", "app/app.py"]
