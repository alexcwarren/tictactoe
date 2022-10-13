# Tic-Tac-Toe app

## To Run

```bash
python tictactoe.py
```

## To Test
```bash
# Console output only
python -m pytest -v

# Consle output and write to logfile
# (PowerShell)
python -m pytest -v *>&1 | Tee-Object -FilePath <path_to_logfile>

# (bash)
python -m pytest -v 2>&1 | tee <path_to_logfile>
```

## To Check Code Quality
```bash
pylama
```

## To Format Code
```bash
# Sort imports
isort .

# Format according to PEP 8
black .
```