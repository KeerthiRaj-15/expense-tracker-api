import json
from pathlib import Path

# Path to expenses.json
DATA_FILE = Path(__file__).parent / "expenses.json"


def load_expenses():
    """Load all expenses from JSON file."""
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_expenses(expenses):
    """Save all expenses to JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)