from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.main import app
from fastapi.testclient import TestClient

client = TestClient(app)




def test_add_expense():
    response = client.post(
        "/expenses",
        json={
            "id": 10,
            "title": "Book",
            "amount": 500,
            "category": "Education",
            "date": "2026-08-01"
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Expense added successfully"


def test_get_all_expenses():
    response = client.get("/expenses")

    assert response.status_code == 200
    assert isinstance(response.json(), list)



def test_filter_by_category():
    response = client.get("/expenses/category/Food")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_total_expenses():
    response = client.get("/expenses/total")

    assert response.status_code == 200
    assert "total" in response.json()



def test_total_by_category():
    response = client.get("/expenses/total/Food")

    assert response.status_code == 200
    assert "total" in response.json()


def test_delete_expense():
    response = client.delete("/expenses/10")

    assert response.status_code == 200