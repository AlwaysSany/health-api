#!/bin/bash
set -e

echo "Running tests..."

# Run tests with coverage
uv run pytest tests/ -v --cov=app --cov-report=term-missing --cov-report=html

echo "Tests completed!"