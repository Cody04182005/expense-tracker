# Expense Tracker - Stage 1 (initial version)
# Lets the user record expenses by category and view totals.


def add_expense(expenses, category, amount):
    """Add an amount to a category's running total.

    `expenses` is a dictionary mapping category name -> total spent.
    Using .get(category, 0) means a new category starts at zero, so we
    don't need a separate "does it exist yet?" check.
    """
    expenses[category] = expenses.get(category, 0) + amount


def show_summary(expenses):
    """Print every category total and the grand total."""
    if not expenses:
        print("No expenses recorded yet.")
        return

    grand_total = 0
    print("\n--- Expense Summary ---")
    for category, total in expenses.items():
        print(f"{category}: ${total:.2f}")
        grand_total += total
    print(f"Grand total: ${grand_total:.2f}")


def main():
    expenses = {}  # all data lives in memory; it resets when the program exits

    # Repeat the menu until the user selects the exit option.
    while True:
        print("\n1. Add expense")
        print("2. View summary")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            category = input("Category (e.g. food, rent): ").strip().lower()
            amount = float(input("Amount: "))
            add_expense(expenses, category, amount)
            print("Expense added.")
        elif choice == "2":
            show_summary(expenses)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please enter 1, 2, or 3.")


main()
