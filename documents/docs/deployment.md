## Deployment

### Virtual Environment Usage

- **Virtual Environments** (`venv`, `conda`):
  - In development, using a virtual environment is crucial for managing package versions and isolating your project's dependencies. However, in a Dockerized environment, the Docker container itself acts like a virtual environment, isolating your application and its dependencies from the host system.
  - Therefore, you do not need to activate a virtual environment inside the Docker container. All dependencies should be managed through the Dockerfile and the container's setup.


### 1. Using Uvicorn for Development

Uvicorn is an ASGI server for running Python web apps built with frameworks like FastAPI and Starlette. It's highly efficient and suited for async programming.

#### Setting Up Uvicorn for Development:
- **Command Line**: To run your FastAPI application with Uvicorn during development, you typically use the following command:
  ```bash
  uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
  ```
  - `app.main:app` specifies the Python module and application instance.
  - **`--reload`**: This option is typically used in development environments to automatically restart the server when code changes are detected. It is not used in production because it can reduce performance.
  - **`--host` and `--port`**: These options define the network address and port on which the server will listen. `0.0.0.0` as a host tells Uvicorn to listen on all network interfaces, making the server accessible externally. The port can be any port that's not already in use by another application.

This setup allows you to develop with real-time feedback, as any changes you make to your code will automatically reload the server.

### 2. Future Plan: Scaling Up with Docker Compose

Docker Compose facilitates the orchestration of multi-container Docker environments, allowing us to scale our microservices seamlessly. Initially, we may start with a straightforward Docker setup for our Stock Indicator Microservice. However, as the project evolves, the complexity and the need for additional services such as databases for storing historical stock data or caching services for quick access to frequently requested data may arise.

For instance, if we decide to enhance our microservice to not only fetch but also store historical data, integrating a PostgreSQL database would be a practical step. Docker Compose can manage both the microservice and the database in a unified environment. This setup ensures that each component is properly linked and scalable. Here’s how it might look:

- **Microservice Container**: Runs the FastAPI application.
- **Database Container**: Manages stock data, potentially reducing API call overhead by caching past requests.
- **Cache Container** (like Redis): Speeds up response times for frequently accessed data.

Post-completion of the initial project phase and delivery this exercise to my senior, I plan to explore and implement Docker Compose during my free time. This exploration will not only enhance my understanding of container orchestration but also prepare me for future CI/CD implementations that I'll learn from my senior later in the internship.

### 3. Docker Workflow: Build, Push, and Run

#### Building and Pushing to Docker Hub
- **Building an Image**:
  - Navigate to your project directory (where the Dockerfile is located).
  - Run the following command:
    ```bash
    docker build -t mewakin/mlops-clean-code-project .
    ```
    This command builds the Docker image and tags it with your Docker Hub username and a name for the repository.

- **Pushing to Docker Hub**:
  - First, log in to Docker Hub from the command line:
    ```bash
    docker login
    ```
  - Push your image:
    ```bash
    docker push mewakin/mlops-clean-code-project
    ```

#### Running the Image
- After pushing the image to Docker Hub, you or anyone else can run it:
  ```bash
  docker run -p 8000:8000 mewakin/mlops-clean-code-project
  ```
  This command runs your Docker container and maps port 8000 of the container to port 8000 on your host, allowing you to access the FastAPI app through your local machine’s IP.

### 4. Interacting with the Application Using Postman

- **Setting Up Postman**:
  - Create a new request in Postman.
  - Set the request URL to your FastAPI app's endpoint, e.g., `http://localhost:8000/<endpoint>`.
  - Choose the appropriate HTTP method (GET, POST, etc.).
  - Add any required headers or body data.
  - Send the request and view the response.

<<<<<<< HEAD
Using Postman, you can test all the API endpoints in your application, ensuring they work as expected before and after deploying your Docker container.
=======
In development phase, using Postman, you can test all the API endpoints in your application, ensuring they work as expected before and after deploying your Docker container.

will do API test with pytest too
>>>>>>> new-main
