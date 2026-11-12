# Expense Tracker - Stage 2 (Manual improvements)
# New in this version:
#   * Input validation (no crashes on text, rejects zero/negative amounts)
#   * Summary is sorted from highest to lowest spending
#   * New menu option that reports the top spending category

import json
import os

DATA_FILE = "expenses.json"


def add_expense(expenses, category, amount):
    """Add an amount to a category's running total.

    `expenses` is a dictionary mapping category name -> total spent.
    """
    expenses[category] = expenses.get(category, 0) + amount


def get_valid_amount():
    """Keep asking until the user enters a positive number.

    Stage 2 change: Stage 1 called float() directly, which crashed the
    program on input like "abc". Here a try/except catches the error and
    the loop re-prompts instead.
    """
    while True:
        text = input("Amount: ")
        try:
            amount = float(text)
        except ValueError:
            print("Please enter a number (for example 12.50).")
            continue
        if amount <= 0:
            print("Amount must be greater than zero.")
            continue
        return amount


def get_valid_category():
    """Keep asking until the user enters a non-empty category name."""
    while True:
        category = input("Category (e.g. food, rent): ").strip().lower()
        if category:
            return category
        print("Category cannot be empty.")


def show_summary(expenses):
    """Print category totals sorted from highest to lowest, then the grand total.

    Stage 2 change: sorted() with key=lambda item: item[1] orders the
    (category, total) pairs by total; reverse=True puts the largest first.
    """
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- Expense Summary (highest first) ---")
    for category, total in sorted(expenses.items(), key=lambda item: item[1], reverse=True):
        print(f"{category}: ${total:.2f}")
    print(f"Grand total: ${sum(expenses.values()):.2f}")


def show_top_category(expenses):
    """Report which category has the highest total and its share of spending.

    Stage 2 addition. max() with key=expenses.get compares categories by
    their totals rather than alphabetically.
    """
    if not expenses:
        print("No expenses recorded yet.")
        return

    top = max(expenses, key=expenses.get)
    share = expenses[top] / sum(expenses.values()) * 100
    print(f"Top category: {top} (${expenses[top]:.2f}, {share:.1f}% of all spending)")


def remove_category(expenses):
    """Delete a whole category (and its total) after the user types its name."""
    if not expenses:
        print("No expenses recorded yet.")
        return

    category = input("Category to remove: ").strip().lower()
    if category in expenses:
        # pop() removes the key from the dictionary and returns its value
        removed_total = expenses.pop(category)
        print(f"Removed '{category}' (${removed_total:.2f}).")
    else:
        print(f"Category '{category}' not found.")


def load_expenses():
    """Load saved expenses from DATA_FILE. Return {} if missing or unreadable."""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        return {str(category): float(total) for category, total in data.items()}
    except (OSError, ValueError, TypeError, AttributeError):
        print("Could not read saved expenses; starting with an empty list.")
        return {}


def save_expenses(expenses):
    """Write the expenses dictionary to DATA_FILE as JSON."""
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(expenses, f, indent=2)
    except OSError:
        print("Warning: could not save expenses to disk.")


def main():
    expenses = load_expenses()  # restore data saved by a previous run

    # Repeat the menu until the user selects the exit option.
    while True:
        print("\n1. Add expense")
        print("2. View summary")
        print("3. Show top spending category")
        print("4. Remove a category")
        print("5. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            category = get_valid_category()
            amount = get_valid_amount()
            add_expense(expenses, category, amount)
            print("Expense added.")
        elif choice == "2":
            show_summary(expenses)
        elif choice == "3":
            show_top_category(expenses)
        elif choice == "4":
            remove_category(expenses)
        elif choice == "5":
            save_expenses(expenses)
            print("Expenses saved. Goodbye!")
            break
        else:
            print("Invalid option, please enter 1, 2, 3, 4, or 5.")


main()