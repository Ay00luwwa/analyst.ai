import sqlite3
from tabulate import tabulate  # Install with: pip install tabulate

class ExpenseTracker:
    def __init__(self, db_path="expense_tracker.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            amount REAL
        );
        '''
        self.conn.execute(query)
        self.conn.commit()

    def add_expense(self, category, amount):
        query = "INSERT INTO expenses (category, amount) VALUES (?, ?);"
        self.conn.execute(query, (category, amount))
        self.conn.commit()

    def view_expenses(self):
        query = "SELECT * FROM expenses;"
        cursor = self.conn.execute(query)
        expenses = cursor.fetchall()

        if expenses:
            headers = ["ID", "Category", "Amount"]
            table = tabulate(expenses, headers=headers, tablefmt="pretty")
            print(table)
        else:
            print("No expenses recorded.")

    def close_connection(self):
        self.conn.close()

# Example usage
expense_tracker = ExpenseTracker()

while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Quit")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: "))
        expense_tracker.add_expense(category, amount)
        print("Expense added successfully!")
    elif choice == '2':
        expense_tracker.view_expenses()
    elif choice == '3':
        expense_tracker.close_connection()
        break
    else:
        print("Invalid choice. Please try again.")
