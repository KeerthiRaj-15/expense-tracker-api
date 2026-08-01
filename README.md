# Smart Expense Tracker API

A RESTful API built using **FastAPI** to manage personal expenses. This project allows users to add, view, filter, calculate totals, and delete expenses. Data is stored locally in a JSON file without using a database.

---

## Features

- Add a new expense
- View all expenses
- Filter expenses by category
- Calculate total expenses
- Calculate total expenses by category
- Delete an expense
- Interactive API documentation using Swagger UI

---

## Tech Stack

- Python 3.12
- FastAPI
- Uvicorn
- Pytest

---

## Project Structure

```text
expense-tracker-api/
│
├── README.md
├── AI_NOTES.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── storage.py
│   └── expenses.json
│
└── tests/
    ├── __init__.py
    └── test_api.py
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/KeerthiRaj-15/expense-tracker-api.git
```

Move into the project folder

```bash
cd expense-tracker-api
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Server

```bash
python -m uvicorn src.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## Running Tests

Run all tests:

```bash
python -m pytest
```

Expected output:

```text
=============================
6 passed
=============================
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/expenses` | Add a new expense |
| GET | `/expenses` | View all expenses |
| GET | `/expenses/category/{category}` | Filter expenses by category |
| GET | `/expenses/total` | Calculate total expenses |
| GET | `/expenses/total/{category}` | Calculate total expenses by category |
| DELETE | `/expenses/{expense_id}` | Delete an expense |

---

## Testing

The application includes automated tests for:

- Add Expense
- View All Expenses
- Filter by Category
- Calculate Total Expenses
- Calculate Total by Category
- Delete Expense

Run:

```bash
python -m pytest
```

---

## Bonus Feature

This project includes **Swagger/OpenAPI Documentation**, which provides an interactive interface for testing and exploring all API endpoints.

---

## Author

Keerthi Raj
