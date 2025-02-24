# Bridgarr Backend

## Overview
This project is a Django-based web application with multiple apps including authentication, contract management, vendor management, and wallet functionalities.

## Installation
To install the project, follow these steps:

1. Clone the repository
2. Install the version of Python specified in the `.python-version` file
3. Install poetry by running `pip install poetry`
   > NOTE: You don't need to create a virtual environment. Poetry will handle that for you.
4. Install the project dependencies by running `poetry install`
5. Create a `.env` file in the root of the project and add the environment variables specified in the [Environment Variables](#environment-variables) section
6. Run the project by running `make run` or `poetry run python manage.py runserver`

## Environment Variables
The following environment variables are required to run the project:
- `DJANGO_SECRET_KEY`: The secret key used by Django to secure the project
- `DJANGO_ADMIN_URL`: The URL used to access the Django admin panel (you can set this to `admin/` for example)
- `DJANGO_ALLOWED_HOSTS`: The allowed hosts for the project (comma-separated). This is not required for development.
- `CORS_ALLOWED_ORIGINS`: The allowed origins for CORS (comma-separated). This is not required for development.
- `DATABASE_URL`: The URL of the database to use. This should be in the format `postgres://<user>:<password>@host:port/dbname`. This is only required for production.
- `FRONTEND_URL`: The URL of the frontend application.

Any environment variable not listed here, you can find in the [`.env.example` file](.env.example).

## Makefile Commands
The following commands are available in the Makefile:

- `make run`: Run the Django development server
- `make shell`: Open a Django shell
- `make db-upgrade`: Make migrations and migrate the database
- `make db-flush`: Flush all data from the database
- `make db-migrate`: Apply migrations to the database
- `make requirements`: Compile the project requirements to the `requirements.txt` file