# MyPackage — Python Utility Package

A simple Python utility package built and installed locally. Demonstrates how to structure, build and distribute a Python package.

## What it does

- `greet(name)` — returns a personalised greeting
- `calculate_total(items)` — calculates total price from a list of order items
- `format_naira(amount)` — formats a number as NGN currency

## Tech Stack

- Python 3
- setuptools — package building and installation

## Installing Locally
```bash
pip install -e .
```

## Usage
```python
from mypackage import greet, calculate_total, format_naira

print(greet("Bolzy"))
# Hello, Bolzy! Welcome to MyPackage.

print(format_naira(calculate_total([
    {"price": 8500, "qty": 2},
    {"price": 3200, "qty": 1}
])))
# NGN 20,200.00
```

## Package Structure
```
mypackage/
├── setup.py
├── README.md
└── mypackage/
    ├── __init__.py
    └── utils.py
```

## Key Concepts

- **Package structure** — `__init__.py` makes a folder a Python package
- **`setup.py`** — defines package metadata and entry points
- **`pip install -e .`** — installs package in editable mode for local development
- **Importing from a package** — clean imports via `__init__.py`

## Author

**Omobolanle Sadela**  
[GitHub](https://github.com/bolanlesadela) · [LinkedIn](https://www.linkedin.com/in/omobolanle-sadela-7a486a1b4/)
