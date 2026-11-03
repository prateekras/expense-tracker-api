# Expense Tracker API

A lightweight RESTful API for managing personal expenses, built with **Python, FastAPI, SQLAlchemy, and SQLite**.

This project was developed as a hands-on backend learning project to practise API design, CRUD operations, data validation, database integration, filtering, pagination, aggregation, and automated testing.

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Tests](https://img.shields.io/badge/Tests-3%20passed-brightgreen)](#run-tests)

## Overview

The API allows users to create and manage expense records, retrieve expenses with optional filters, and view a monthly spending summary. FastAPI provides interactive API documentation, while SQLAlchemy handles database operations and Pydantic validates request data.

> **Project scope:** This is a learning project intended to demonstrate backend fundamentals. It is not a production-ready financial application and does not currently implement user authentication or multi-user data isolation.

## Features

- **Expense CRUD:** create, list, retrieve, update, and delete expense records
- **Input validation:** validate request payloads using Pydantic schemas
- **Database integration:** persist records in SQLite using SQLAlchemy ORM
- **Filtering:** filter expenses by category and date range
- **Pagination:** control list results with `limit` and `offset`
- **Monthly summary:** calculate total spending and expense count for a selected month
- **Interactive documentation:** explore and test endpoints through Swagger UI
- **Automated tests:** API tests written with pytest and HTTPX

## Tech stack

| Area | Technology |
|---|---|
| Language | Python 3.12 |
| API framework | FastAPI |
| ORM | SQLAlchemy |
| Database | SQLite |
| Validation | Pydantic |
| Testing | Pytest, HTTPX |
| API documentation | Swagger UI (OpenAPI) |

## Getting started

### Prerequisites

- Python 3.12
- Git

### Installation (Windows)

1. Clone the repository:

   ```cmd
   git clone https://github.com/prateekras/expense-tracker-api.git
   cd expense-tracker-api
   ```

2. Create and activate a virtual environment:

   ```cmd
   py -3.12 -m venv .venv
   .venv\\Scripts\\activate
   ```

3. Install dependencies:

   ```cmd
   python -m pip install -r requirements.txt
   ```

4. Start the development server:

   ```cmd
   python -m uvicorn app.main:app --reload
   ```

5. Open the interactive API documentation:

   **http://127.0.0.1:8000/docs**

The SQLite database file (`expenses.db`) is created automatically in the project directory when the application starts.

## API reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Welcome message |
| `GET` | `/health` | Health check |
| `POST` | `/expenses` | Create an expense |
| `GET` | `/expenses` | List expenses with optional filters and pagination |
| `GET` | `/expenses/{expense_id}` | Retrieve one expense |
| `PATCH` | `/expenses/{expense_id}` | Update selected expense fields |
| `DELETE` | `/expenses/{expense_id}` | Delete an expense |
| `GET` | `/summary/{year}/{month}` | Get monthly spending total and expense count |

### Example: create an expense

Send a `POST /expenses` request with:

```json
{
  "title": "Lunch",
  "amount": "250.00",
  "category": "Food",
  "description": "Lunch at college",
  "spent_on": "2026-11-03"
}
```

The `spent_on` field is optional; if omitted, the application uses the current date.

### Example: list expenses

```http
GET /expenses?category=Food&limit=10&offset=0
```

### Example: monthly summary

```http
GET /summary/2026/11
```

## Run tests

With the virtual environment activated, run:

```cmd
python -m pytest -q
```

**Local test result:** 3 tests passed. A dependency deprecation warning was reported, but it did not cause any test failures.

The tests use a separate in-memory SQLite database and do not modify local expense records.

## Project structure

```text
expense-tracker-api/
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── tests/
│   └── test_api.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Key learning outcomes

- Designing RESTful endpoints and choosing appropriate HTTP methods
- Structuring a FastAPI application
- Defining database models and working with SQLAlchemy sessions
- Validating request and response data with Pydantic
- Implementing filtering, pagination, and aggregation queries
- Writing automated API tests and checking response codes

## Future improvements

- Add user registration, authentication, and per-user expense records
- Add stronger test coverage for validation and error cases
- Add database migrations
- Add Docker support and a deployment workflow
- Add CI checks with GitHub Actions

## Author

**Prateek Rastogi**  
GitHub: [@prateekras](https://github.com/prateekras)
