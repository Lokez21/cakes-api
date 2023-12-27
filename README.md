# Cakes API Application
Welcome to My Cakes API django project! This README provides instructions on how to create and run a Docker image for this project.

## Prerequisites
Make sure you have the following installed on your machine:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Project Structure
```
/cakes
|-- /cakes
| |-- settings.py
| |-- ...
|-- Dockerfile
|-- docker-compose.yml
|-- requirements.txt
|-- manage.py
|-- readme.md
|-- requirements.txt
```

## Building and Running the Docker Image
*Here is the guide for building docker image from the dockerfile located in the application's root and then creating a container and running the container.* 

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Lokez21/cakes-api.git

2. **Navigate to the root of the project directory:**
   ```bash
   cd cakes

3. **Build the Docker Image:**
   ```bash
   docker-compose build

4. **Run the Docker Container:**
   ```bash
   docker-compose up

5. The application will be accessible at http://localhost:8000

## Recommended API tool
The Cakes API application home page hosts the swagger/openAPI documentation.

Postman is recommended to test the API methods. You can download it here:
- [Download Postman](https://www.postman.com/downloads/)

#### Exposed endpoints
- http://localhost:8000 (Method: GET) - Swagger/OpenAPI documentation
- http://localhost:8000/list_all_cakes/ (Method: GET)
- http://localhost:8000/select_cake/2 (Method: GET)
- http://localhost:8000/add_cake/ (Method: POST)
- http://localhost:8000/update_cake/2?name=vanilla_cake&comment=test (Method: PATCH)
- http://127.0.0.1:8000/delete_cake/10 (Method: DELETE)
