
# Health Microservice API

A comprehensive FastAPI microservice for health-related operations with JWT authentication, PostgreSQL database, and Alembic migrations. Built with UV package manager for fast dependency management.

## Working Demo

[health-api-mcp-server-with-fastapi-demo.webm](https://github.com/user-attachments/assets/49dee391-a380-4c66-b7b9-f27ce44c2836)

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

- Python 3.13.3+
- PostgreSQL
- UV package manager

## Project Structure

The project follows a modular structure suitable for large applications with clear separation of concerns between models, schemas, routes, and business logic.

![project_structure](https://github.com/user-attachments/assets/496bd188-ba19-40ff-80e1-05abc6882966)

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
uv run uvicorn app.main:app --host 0.0.0.0 --port 5000 --reload
# Or use the convenience script
chmod +x scripts/start.sh
./scripts/start.sh
```

## Some more required alembic migration commands

These commands are not required during setup but are useful for managing migrations in the future
during development.

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

- Swagger UI: http://localhost:5000/docs
- ReDoc: http://localhost:5000/redoc

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

## Main API Endpoints (after authentication)

After obtaining a JWT access token, you can access the following endpoints:

### Doctors
- `GET /doctors` — List all doctors
- `GET /doctors/{doctor_id}` — Get a specific doctor by ID
- `POST /doctors` — Create a new doctor
- `PUT /doctors/{doctor_id}` — Update a doctor's information
- `DELETE /doctors/{doctor_id}` — Delete a doctor

### Patients
- `GET /patients` — List all patients
- `GET /patients/{patient_id}` — Get a specific patient by ID
- `POST /patients` — Create a new patient
- `PUT /patients/{patient_id}` — Update a patient's information
- `DELETE /patients/{patient_id}` — Delete a patient

### Medical Records
- `GET /medical-records` — List all medical records (optionally filter by patient)
- `GET /medical-records/{record_id}` — Get a specific medical record by ID
- `POST /medical-records` — Create a new medical record
- `PUT /medical-records/{record_id}` — Update a medical record
- `DELETE /medical-records/{record_id}` — Delete a medical record

### Appointments
- `GET /appointments` — List all appointments
- `GET /appointments/{appointment_id}` — Get a specific appointment by ID
- `POST /appointments` — Create a new appointment
- `PUT /appointments/{appointment_id}` — Update an appointment
- `DELETE /appointments/{appointment_id}` — Delete an appointment

All these endpoints require the `Authorization: Bearer <token>` header. Refer to the interactive API docs at `/docs` for detailed request/response schemas and try out the endpoints interactively.

## Package Management with UV

UV provides fast dependency resolution and installation. Useful commands:

- `uv sync` - Install dependencies from lock file
- `uv add <package>` - Add a new dependency
- `uv remove <package>` - Remove a dependency
- `uv run <command>` - Run command in virtual environment
- `uv lock` - Update the lock file

## Contributing

1. Install development dependencies: `uv sync --group dev`
2. Make your changes
3. Run tests: `uv run pytest`
4. Format code: `uv run black app/ tests/`
5. Submit a pull request

## MCP Integration

Integration with MCP is done by using the `FastApiMCP` class from the `fastapi_mcp` package. The MCP server is mounted to the FastAPI application using the `mount` method.

`windsurf` settings,

```json 
{
  "mcpServers": {
    "health-api": {
      "serverUrl": "http://localhost:5000/mcp",
      "headers": {
        "Authorization": "Bearer <put_your_bearer_token_here>"
      } 
    }
  }
}
```

`vscode` or `cursor` settings,

```json
{
  "servers": {
    "health-api": {
      "url": "http://localhost:5000/mcp",
      "headers": {
        "Authorization": "Bearer <put_your_bearer_token_here>"
      }
    }
  }
}
```

Note: I haven't tested on `vscode` or `cursor` yet.

## License

MIT License

## Contact

- Author: [Sany Ahmed](https://github.com/sany2k8)
- Email: sany2k8@gmail.com

## References
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Python](https://www.python.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [UV](https://astral.sh/uv/)
- [JWT](https://jwt.io/)
