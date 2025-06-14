# Health Microservice API

A comprehensive FastAPI microservice for health-related operations with JWT authentication, PostgreSQL database, and Alembic migrations. Built with UV package manager for fast dependency management.

## Features

- JWT-based authentication
- PostgreSQL database with async SQLAlchemy
- Alembic database migrations
- Comprehensive health domain models (Patient, Doctor, Appointment, Medical Record)
- RESTful API endpoints
- Interactive API documentation (Swagger UI)
- Modular project structure
- CORS middleware
- Async/await support
- UV package manager for fast dependency resolution
- Comprehensive test suite

## Prerequisites

- Python 3.11+
- PostgreSQL
- UV package manager

## Installation

### Install UV

```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or with pip
pip install uv
```

## Setup Project

Clone the repository:

```bash
git clone <repository-url>
cd health-api
```

Install dependencies:

```bash
uv sync
```

Set up environment variables:

```bash
cp .env.example .env
# Edit .env with your database credentials and secret key
```

## Database Migrations with Alembic (using UV)

Alembic is used for handling database migrations. All commands below assume you are in the project root directory.

But first off all create up a PostgreSQL database:

```sql
CREATE DATABASE health_db;
```

### Generate a New Migration (Autogenerate)

```bash
uv run alembic revision --autogenerate -m "Your migration message"
```

### Apply Migrations (Upgrade Database)

```bash
uv run alembic upgrade head
```

Start the application (choose one):

```bash
uv run uvicorn app.main:app --port 5000 --reload
# Or use the convenience script
chmod +x scripts/start.sh
./scripts/start.sh
```

## Some more required alembic migration commands

#### Downgrade Database (Revert Last Migration)

```bash
uv run alembic downgrade -1
```

#### View Current Migration Status

```bash
uv run alembic current
```

#### Show Migration History

```bash
uv run alembic history
```

For more Alembic commands and usage, see the [Alembic documentation](https://alembic.sqlalchemy.org/en/latest/).


## Development

Install development dependencies:

```bash
uv sync --group dev
```

Run tests:

```bash
uv run pytest
# Or use the test script
chmod +x scripts/test.sh
./scripts/test.sh
```

Code formatting:

```bash
uv run black app/ tests/
uv run isort app/ tests/
```

Type checking:

```bash
uv run mypy app/
```

## Docker

Build and run with Docker Compose:

```bash
docker-compose up --build
```

This will start both the PostgreSQL database and the FastAPI application.

## API Documentation

Once the application is running, visit:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Database Migrations

Create a new migration:

```bash
uv run alembic revision --autogenerate -m "Description of changes"
# Or use the migration script
chmod +x scripts/migrate.sh
./scripts/migrate.sh "Description of changes"
```

Apply migrations:

```bash
uv run alembic upgrade head
```

## Authentication

- Register a new user: `POST /auth/register`
- Login to get access token: `POST /auth/login`
- Use the token in Authorization header: `Bearer <token>`

## Package Management with UV

UV provides fast dependency resolution and installation. Useful commands:

- `uv sync` - Install dependencies from lock file
- `uv add <package>` - Add a new dependency
- `uv remove <package>` - Remove a dependency
- `uv run <command>` - Run command in virtual environment
- `uv lock` - Update the lock file

## Project Structure

The project follows a modular structure suitable for large applications with clear separation of concerns between models, schemas, routes, and business logic.

## Contributing

1. Install development dependencies: `uv sync --group dev`
2. Make your changes
3. Run tests: `uv run pytest`
4. Format code: `uv run black app/ tests/`
5. Submit a pull request

## License

MIT License