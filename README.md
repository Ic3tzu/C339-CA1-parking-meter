# Project 03: Parking Meter System

Unit tests for the C339 CA1 assessment. The code under test has two functions:

| File | Function | What it does |
|---|---|---|
| `src/parking_fee.py` | `calculate_parking_fee(minutes)` | Charges 200 cents for every started hour |
| `src/parking_permit.py` | `is_permit_valid(permit_active, parked_minutes)` | Returns `True` only for an active permit and a stay of at most 120 minutes |

The tests are written from the requirements specification (`parking_meter-specification.pdf`), not from the code.

## Folder structure

```
03_parking_meter/
├── .github/
│   └── workflows/
│       └── tests.yml          # GitHub Actions workflow
├── src/
│   ├── parking_fee.py         # supplied source file (unchanged)
│   └── parking_permit.py      # supplied source file (unchanged)
├── tests/
│   ├── test_parking_fee.py
│   └── test_parking_permit.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Run the tests

Run these from the project root, the folder that contains `src` and `tests`.

```
pip install -r requirements.txt
python -m pytest -v
python -m pytest --cov=src --cov-report=term-missing
```

## GitHub Actions

The workflow in `.github/workflows/tests.yml` runs the tests automatically.

- It runs on pushes to `main` and on pull requests into `main`.
- It only runs when `src/`, `tests/`, `requirements.txt` or the workflow file changes.
- A newer push cancels an older run that is still in progress.
