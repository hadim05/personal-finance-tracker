from database import create_table, add_transaction, get_transactions

def show_menu():
    print("\nPersonal Finance Tracker")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Exit")

def main():
    create_table()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            category = input("Enter income category: ")
            amount = float(input("Enter amount: "))
            add_transaction("Income", category, amount)
            print("Income added successfully.")

        elif choice == "2":
            category = input("Enter expense category: ")
            amount = float(input("Enter amount: "))
            add_transaction("Expense", category, amount)
            print("Expense added successfully.")

        elif choice == "3":
            transactions = get_transactions()
            print("\nTransactions:")
            for t in transactions:
                print(t)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
