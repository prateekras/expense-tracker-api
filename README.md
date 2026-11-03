# Expense Tracker API

A REST API built with **Python, FastAPI, SQLAlchemy and SQLite**. It lets a user record expenses, browse and filter them, edit or delete records, and view a monthly spending summary.

> Learning project: built for practising Python backend development and REST API fundamentals. It is not an authenticated production finance application.

## Features

- Create, list, view, update and delete expenses (CRUD)
- Validate request data with Pydantic
- Store data in SQLite through SQLAlchemy ORM
- Filter expenses by category and date range
- Paginate the expense list with `limit` and `offset`
- Calculate monthly spending total and number of expenses
- Interactive API documentation through Swagger UI
- Automated API tests using pytest

## Tech stack

- Python 3.10+
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Pytest and HTTPX

## Run locally (Windows)

1. Install Python 3.10 or newer.
2. Clone this repository and open its folder in a terminal.
3. Create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .venv\Scripts\activate
   ```

4. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

5. Start the development server:

   ```powershell
   uvicorn app.main:app --reload
   ```

6. Open **http://127.0.0.1:8000/docs** for interactive API documentation.

The SQLite database file (`expenses.db`) is created automatically in the project folder when the app starts.

## API endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/health` | Health check |
| POST | `/expenses` | Create an expense |
| GET | `/expenses` | List expenses; optional category/date filters and pagination |
| GET | `/expenses/{expense_id}` | Get one expense |
| PATCH | `/expenses/{expense_id}` | Update selected fields |
| DELETE | `/expenses/{expense_id}` | Delete an expense |
| GET | `/summary/{year}/{month}` | Monthly total and expense count |

## Example: create an expense

Send a `POST /expenses` request with JSON:

```json
{
  "title": "Lunch",
  "amount": "250.00",
  "category": "Food",
  "description": "Lunch at college",
  "spent_on": "2026-11-03"
}
```

The `spent_on` field is optional; if omitted, today's date is used.

## Run tests

With the virtual environment active:

```powershell
pytest -q
```

Tests use a separate in-memory SQLite database, so they do not modify your local expense records.

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

## What I learned

This project is intended to demonstrate REST conventions, CRUD operations, request validation, database sessions, ORM models, filtering, pagination, aggregation queries and automated endpoint testing.
