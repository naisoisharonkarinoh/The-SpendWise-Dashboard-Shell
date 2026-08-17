#!/usr/bin/env python3
"""Simple menu-driven expense manager backed by a list of dictionaries."""

from collections import defaultdict
from typing import List, Dict


def seed_expenses() -> List[Dict]:
    return [
        {"amount": 12.50, "desc": "Lunch", "category": "Food"},
        {"amount": 45.00, "desc": "Groceries", "category": "Food"},
        {"amount": 9.99, "desc": "Bus ticket", "category": "Transport"},
        {"amount": 120.00, "desc": "New headphones", "category": "Electronics"},
    ]


def prompt_amount() -> float:
    while True:
        raw = input("Amount: ").strip()
        try:
            amt = float(raw)
        except ValueError:
            print("Please enter a valid number for the amount.")
            continue
        if amt <= 0:
            print("Amount must be greater than 0.")
            continue
        return amt


def prompt_nonempty(prompt: str) -> str:
    while True:
        v = input(prompt).strip()
        if not v:
            print("This field cannot be empty.")
            continue
        return v


def add_expense(expenses: List[Dict]):
    print("Add expense — press Ctrl+C to cancel")
    try:
        amount = prompt_amount()
    except KeyboardInterrupt:
        print("\nAdd cancelled.")
        return
    desc = prompt_nonempty("Description: ")
    category = prompt_nonempty("Category: ")
    expenses.append({"amount": amount, "desc": desc, "category": category})
    print("Expense added.")


def list_expenses(expenses: List[Dict]):
    if not expenses:
        print("No expenses recorded yet.")
        return
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. ${e['amount']:.2f} - {e['desc']} [{e['category']}]")


def filter_by_category(expenses: List[Dict]):
    cat = input("Category to filter: ").strip()
    if not cat:
        print("Category cannot be empty.")
        return
    matches = [e for e in expenses if e["category"].lower() == cat.lower()]
    if not matches:
        print(f"No expenses found for category '{cat}'.")
        return
    for i, e in enumerate(matches, start=1):
        print(f"{i}. ${e['amount']:.2f} - {e['desc']} [{e['category']}]")


def summary(expenses: List[Dict]):
    if not expenses:
        print("No expenses to summarize.")
        return
    total = sum(e["amount"] for e in expenses)
    count = len(expenses)
    average = total / count if count else 0
    largest = max(expenses, key=lambda e: e["amount"])
    per_cat = defaultdict(float)
    for e in expenses:
        per_cat[e["category"]] += e["amount"]

    print(f"Total: ${total:.2f}")
    print(f"Count: {count}")
    print(f"Average: ${average:.2f}")
    print(f"Largest: ${largest['amount']:.2f} - {largest['desc']} [{largest['category']}]")
    print("Per-category totals:")
    for cat, amt in per_cat.items():
        print(f" - {cat}: ${amt:.2f}")


def main():
    expenses = seed_expenses()
    while True:
        print("\nExpense Manager")
        print("1) Add expense")
        print("2) List all")
        print("3) Filter by category")
        print("4) Summary")
        print("5) Quit")
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            filter_by_category(expenses)
        elif choice == "4":
            summary(expenses)
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice — enter a number from 1 to 5.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting.")
