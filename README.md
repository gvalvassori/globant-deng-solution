# Globant's Data Engineering Coding Challenge

## Overview

This repository contains the solution for Globant's Data Engineering Coding Challenge. The challenge involves creating a local REST API for a database migration with three different tables: departments, jobs, and employees. The API should be able to receive historical data from CSV files, upload these files to the new database, and support batch transactions with one request.

## Frameworks Used

The main frameworks used in this project are:

- FastAPI
- Pydantic
- SQLAlchemy
- Alembic
- Pytest

## Layered Architecture

The solution follows a layered architecture, which separates the concerns of the application into different layers. The layers used in this project are:

1. Presentation Layer: This layer handles the API endpoints and request/response handling. It is implemented using FastAPI and Pydantic.
2. Business Logic Layer: This layer contains the business logic of the application, including data validation, transformation, and database operations. It is implemented using Python modules and functions.
3. Data Access Layer: This layer is responsible for interacting with the database. It uses SQLAlchemy to perform database operations such as querying and inserting data.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository from GitHub.
2. Run `docker compose build`
3. Run `docker compose up app`
4. Run `docker compose run migrations` -> This runs the database migrations

## API Endpoints

The following API endpoints are available:

- Three `POST` endpoints to load the csv files
- Two `GET` endpoints to get reports
