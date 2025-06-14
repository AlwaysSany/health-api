#!/bin/bash
set -e

if [ -z "$1" ]; then
    echo "Usage: $0 <migration_message>"
    exit 1
fi

echo "Creating new migration: $1"
uv run alembic revision --autogenerate -m "$1"

echo "Migration created successfully!"