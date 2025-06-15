# Contributing to Health Microservice API

Thank you for considering contributing to this project! Your help is greatly appreciated. Please follow the guidelines below to ensure a smooth contribution process.

## Getting Started

1. **Fork the repository** and clone it to your local machine.
2. **Install dependencies** using [UV](https://astral.sh/uv/):
   ```bash
   uv sync --group dev
   ```
3. **Set up your environment variables** by copying `.env.example` to `.env` and editing as needed.
4. **Run tests** to ensure everything is working:
   ```bash
   uv run pytest
   ```

## Making Changes

- Keep your code clean and well-documented.
- Write meaningful commit messages.
- Add or update tests for your changes.
- Format your code using Black and isort:
  ```bash
  uv run black app/ tests/
  uv run isort app/ tests/
  ```

## Submitting a Pull Request

1. Ensure all tests pass locally.
2. Push your branch to your forked repository.
3. Open a pull request (PR) against the `main` branch.
4. Provide a clear description of your changes and reference any related issues.

## Code of Conduct

Please be respectful and considerate in all interactions. For more details, refer to the [Contributor Covenant](https://www.contributor-covenant.org/).

## Reporting Issues

If you find a bug or have a feature request, please open an issue on GitHub with clear steps to reproduce or a detailed description.

## Need Help?

If you have questions, feel free to open an issue or contact the maintainer listed in the README.
