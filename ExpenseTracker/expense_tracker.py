import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, amount, category):
        today = datetime.date.today()
        date_key = today.strftime("%Y-%m-%d")

        if date_key not in self.expenses:
            self.expenses[date_key] = []

        self.expenses[date_key].append({"amount": amount, "category": category})
        print("Expense added successfully.")

    def view_spending_patterns(self):
        if not self.expenses:
            print("No expenses recorded.")
            return

        print("\nSpending Patterns:")
        for date, expenses in sorted(self.expenses.items()):
            total_amount = sum(expense["amount"] for expense in expenses)
            print(f"{date}: Total Amount - {total_amount} | Expenses - {expenses}")

def main():
    expense_tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracking System:")
        print("1. Add Expense")
        print("2. View Spending Patterns")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            try:
                amount = float(input("Enter the expense amount: "))
                category = input("Enter the expense category: ")
                expense_tracker.add_expense(amount, category)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif choice == '2':
            expense_tracker.view_spending_patterns()
        elif choice == '3':
            print("Exiting the expense tracking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
