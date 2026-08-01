from fastapi import APIRouter
from src.models import Expense
from src.storage import load_expenses, save_expenses

router = APIRouter()
@router.post("/expenses")
def add_expense(expense: Expense):
    expenses = load_expenses()

    expenses.append(expense.model_dump(mode="json"))

    save_expenses(expenses)

    return {
        "message": "Expense added successfully",
        "expense": expense
    }
@router.get("/expenses")
def get_expenses():
    return load_expenses()

@router.get("/expenses/category/{category}")
def get_expenses_by_category(category: str):
    expenses = load_expenses()

    filtered = [
        expense
        for expense in expenses
        if expense["category"].lower() == category.lower()
    ]

    return filtered

@router.get("/expenses/total")
def get_total_expenses():
    expenses = load_expenses()

    total = sum(expense["amount"] for expense in expenses)

    return {"total": total}


@router.get("/expenses/total/{category}")
def get_total_by_category(category: str):
    expenses = load_expenses()

    total = sum(
        expense["amount"]
        for expense in expenses
        if expense["category"].lower() == category.lower()
    )

    return {
        "category": category,
        "total": total
    }

@router.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    expenses = load_expenses()

    updated_expenses = [
        expense
        for expense in expenses
        if expense["id"] != expense_id
    ]

    if len(updated_expenses) == len(expenses):
        return {"message": "Expense not found"}

    save_expenses(updated_expenses)

    return {"message": "Expense deleted successfully"}
