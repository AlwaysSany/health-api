#!/bin/bash
set -e

echo "Starting Health Microservice..."

# Activate virtual environment if it exists
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# Run database migrations
echo "Running database migrations..."
uv run alembic upgrade head

# Start the application
echo "Starting FastAPI application..."
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000