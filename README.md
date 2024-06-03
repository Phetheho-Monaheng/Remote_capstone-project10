# Setting up and Running the Application
This guide will walk you through the necessary steps to set up and run the application using venv and Docker.

## Prerequisites
Before you begin, make sure you have the following installed:
- Python
- Docker

## Setup with venv
1. Clone this repository to your local machine.
2. Navigate to the root directory of the repository.
3. Create a virtual environment using venv:
   ```bash
   python3 -m venv venv
4. source venv/bin/activate
5. pip install -r requirements.txt

## Running the Application
1. Once you have set up the environment, you can run the application.
2. First ensure that your virtual environment is activated and run the application.
3. Apply Database Migrations: Before starting the server, apply any pending database migrations.
   ```bash
   python manage.py migrate
4. Start Development Server: 
   ```bash
   python manage.py runserver
5. Navigate to the specified URL in your web browser to access the application.

## Setup with Docker
1. Clone this repository to your local machine.
2. Navigate to the root directory of the repository.
3. Build the Docker image using the following command.
   ```bash
    docker build -t <image_name> 
4. Run the Docker container using the built image.
   ```bash
   docker run -p <host_port>:<container_port> <image_name>
   
Once the application is running, you can access it in your web browse.
