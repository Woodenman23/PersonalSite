# Set base image (host OS)
FROM python:3.10-slim

# By default, listen on port 5000
EXPOSE 8080

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . ./

# Copy model into working directory
COPY home/joe/models/covnext_large.pth /models/dognet-convnext_large.pth

# Specify the command to run on container start
CMD [ "python", "./app.py" ]
