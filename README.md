# Globant's Data Engineering Coding Challenge

## Overview

This repository contains the solution for Globant's Data Engineering Coding Challenge. The challenge involves creating a local REST API for a database migration with three different tables: departments, jobs, and employees. The API should be able to receive historical data from CSV files, upload these files to the new database, and support batch transactions with one request.

## Frameworks Used

The main frameworks used in this project are:

- FastAPI: A modern, fast (high-performance), web framework for building APIs with Python.
- Pydantic: A library for data validation and parsing, used for defining the API's request and response models.
- SQLAlchemy: A SQL toolkit and Object-Relational Mapping (ORM) library for Python, used for interacting with the database.
- Alembic: A database migration tool for SQLAlchemy, used for managing database schema changes.
- Pytest: A testing framework for Python, used for writing unit tests.

## Layered Architecture

The solution follows a layered architecture, which separates the concerns of the application into different layers. The layers used in this project are:

1. Presentation Layer: This layer handles the API endpoints and request/response handling. It is implemented using FastAPI and Pydantic.
2. Business Logic Layer: This layer contains the business logic of the application, including data validation, transformation, and database operations. It is implemented using Python modules and functions.
3. Data Access Layer: This layer is responsible for interacting with the database. It uses SQLAlchemy to perform database operations such as querying and inserting data.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository from GitHub.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Configure the database connection in the `config.py` file.
4. Run the database migrations using Alembic by running `alembic upgrade head`.
5. Start the API server by running `uvicorn main:app --reload`.

### Running with Docker

To run the application using Docker, follow these additional steps:

1. Build the Docker image by running `docker build -t globant-deng .`.
2. Run the Docker container by running `docker run -p 8000:8000 globant-deng`.

### Running Alembic Migrations

To run the Alembic migrations manually, follow these additional steps:

1. Make sure the database connection is configured correctly in the `alembic.ini` file.
2. Run the database migrations using Alembic by running `alembic upgrade head`.

## API Endpoints

The following API endpoints are available:

- `POST /upload`: Uploads historical data from CSV files to the database.
- `POST /batch_insert`: Inserts batch transactions (1 up to 1000 rows) with one request.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the [MIT License](LICENSE).
