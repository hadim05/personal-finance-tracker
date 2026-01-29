from database import create_table, add_transaction, get_transactions, get_monthly_summary

def show_menu():
    print("\nPersonal Finance Tracker")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Monthly Summary")
    print("5. Exit")

def main():
    create_table()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            category = input("Enter income category: ")
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM): ")
            add_transaction("Income", category, amount, date)
            print("Income added successfully.")

        elif choice == "2":
            category = input("Enter expense category: ")
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM): ")
            add_transaction("Expense", category, amount, date)
            print("Expense added successfully.")

        elif choice == "3":
            transactions = get_transactions()
            print("\nTransactions:")
            for t in transactions:
                print(t)

        elif choice == "4":
            month = input("Enter month (YYYY-MM): ")
            summary = get_monthly_summary(month)

            income = 0
            expense = 0

            for s in summary:
                if s[0] == "Income":
                    income = s[1]
                elif s[0] == "Expense":
                    expense = s[1]

            balance = income - expense

            print(f"\nSummary for {month}")
            print(f"Total Income: £{income}")
            print(f"Total Expenses: £{expense}")
            print(f"Balance: £{balance}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")
