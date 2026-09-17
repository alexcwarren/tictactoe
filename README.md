# Tic-Tac-Toe

A small Python Tic-Tac-Toe application with a graphical user interface.

This project was built as a programming exercise with an emphasis on separating application logic into model, view, and controller components.

## Run

Clone the repository and run:

```bash
python tictactoe.py
```

The application uses only Python's standard library at runtime.

## Development Setup

Create and activate a virtual environment if desired, then install the development dependencies:

```bash
pip install -r requirements-dev.txt
```

## Testing

Run the test suite:

```bash
python -m pytest -v
```

Pytest configuration is stored in `pytest.ini`.

## Code Quality

Run Pylama against the application and tests:

```bash
pylama tictactoe.py components tests
```

## Formatting

Sort imports:

```bash
isort .
```

Format the Python code:

```bash
black .
```

## Logging

The application writes runtime logs to:

```text
logs/app.log
```

The `logs` directory is created automatically when needed.

Logging configuration is defined in:

```text
log.conf
```

## Project Structure

```text
components/    Application model, view, and controller
design_docs/   Project design documentation
tests/         Automated tests
tictactoe.py   Application entry point
log.conf       Logging configuration
```

## About This Project

This is a small learning project rather than a production application.

It was useful practice for working with:

- Python GUI development
- model-view-controller-style separation
- automated testing with pytest
- application logging
- linting and formatting tools

## License

Licensed under the MIT License. See [`LICENSE`](LICENSE).
