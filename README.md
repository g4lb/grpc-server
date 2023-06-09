# gRPC Server with Database Example

This is an example project that demonstrates how to create a gRPC server in Python using the gRPC framework, along with integration with a PostgreSQL database using the psycopg2 library.

The server exposes a single gRPC method that returns a random number. The server also stores all previous numbers in a PostgreSQL database.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Clone the repository:

   ```shell
   git clone https://github.com/g4lb/grpc-server.git
   ```
   
2. Build the Docker images:

   ```shell
   docker-compose build
   ```
   
3. Start the containers:

   ```shell
   docker-compose up -d
   ```
   This will start the gRPC server and the PostgreSQL database in separate Docker containers.

4. The gRPC server will be accessible at localhost:50051.

5. You can test the server using a gRPC client, such as BloomRPC.

6. To run the unit tests, execute the following command:
   ```shell
   docker-compose run grpc-server python -m unittest discover
   ```
This command will run all the unit tests in the project.

7. to stop the containers, run:
    ```shell
   docker-compose down
   ```

## Project Structure
The project has the following structure:

1. server.py: The main script that sets up the gRPC server and implements the gRPC service.
2. example.proto: The Protocol Buffers file that defines the gRPC service and message types.
3. example_pb2.py and example_pb2_grpc.py: The Python files generated from the example.proto file.
4. config.json: JSON configuration file for the PostgreSQL database connection.
5. requirements.txt: List of Python dependencies for the project.
6. Dockerfile.server and Dockerfile.database: Dockerfiles for building the server and database Docker images.
7. init.sql: SQL script for initializing the PostgreSQL database and creating the required table.
8. test_server: containing the unit tests for the server.

## A recommended client for testing
1. called BloomRPC (https://appimage.github.io/BloomRPC/)
2. Example:
![Alt text](https://i.ibb.co/8zDdzbR/Screen-Shot-2023-06-09-at-17-54-48.png)