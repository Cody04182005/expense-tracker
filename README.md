# Expense Tracker

## Project Description
A command-line Python program that lets a user record expenses by category and
view spending totals. Its purpose is to help someone see where their money goes.

## Initial Version
The first push was developed independently without AI assistance. It included:
- A menu loop that repeats until the user chooses to quit
- `add_expense()`, a function that stores running totals per category in a dictionary
- `show_summary()`, a function that loops through the dictionary and prints each
  category total plus the grand total
- User input for the menu choice, category name, and amount
- Clear printed output for every action

## AI Tool Used
Claude (Anthropic)

## AI Assistance
I asked the AI to help improve my existing program by (1) preventing crashes and
bad data when the user types invalid amounts, (2) making the summary easier to read
by sorting it, and (3) adding a new menu option that shows the top spending category.
I also asked it to explain how the new code works.

## New or Modified Features
- **Input validation:** `get_valid_amount()` and `get_valid_category()` re-prompt
  until the input is valid. Letters, zero, negative numbers, and empty categories
  no longer crash the program or get saved.
- **Sorted summary:** `show_summary()` now lists categories from highest to lowest spending.
- **Top category option:** new menu item 3 shows the biggest spending category and
  its percentage of total spending.

## Evaluation of AI Output
I accepted the try/except validation loop because it fixed a real crash in my first
version (typing letters as an amount caused a ValueError). I kept the sorting after
learning how `sorted()` uses a `key` function to compare the dictionary's totals.
I accepted `max(expenses, key=expenses.get)` for the top category because it is
short and clear, and I understood that it compares totals rather than names. I tested
each change with valid and invalid input before committing.

## How to Run the Program
1. Install Python 3 from python.org.
2. Download `main.py` from this repository.
3. Open a terminal in the folder containing `main.py`.
4. Run: `python main.py` (or `python3 main.py`)
5. Follow the on-screen menu.
