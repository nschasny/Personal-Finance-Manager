from user import User
from finance import FinanceManager, Expense, Income
from budget import Budget
from report import Report

def main():
    print("Personal Finance Manager")
    print("1. Register")
    print("2. Login")
    choice = input("Choose an option: ")

    users = User.load_users()
    finance_manager = FinanceManager()
    finance_manager.load_data()

    if choice == '1':
        username = input("Enter username: ")
        password = input("Enter password: ")
        new_user = User(username, password)
        User.save_user(new_user)
        print("User registered successfully.")

    elif choice == '2':
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = next((u for u in users if u.username == username), None)
        if user and user.authenticate(password):
            print("Login successful.")
            while True:
                print("1. Add Expense")
                print("2. Add Income")
                print("3. Set Budget")
                print("4. Generate Report")
                print("5. Exit")
                option = input("Choose an option: ")
                if option == '1':
                    category = input("Enter expense category: ")
                    amount = float(input("Enter expense amount: "))
                    description = input("Enter expense description: ")
                    expense = Expense(category, amount, description)
                    finance_manager.add_expense(expense)
                elif option == '2':
                    category = input("Enter income category: ")
                    amount = float(input("Enter income amount: "))
                    income = Income(category, amount)
                    finance_manager.add_income(income)
                elif option == '3':
                    amount = float(input("Enter budget amount: "))
                    budget = Budget(amount)
                    print(f"Budget set to: ${budget.get_budget():.2f}")
                elif option == '4':
                    report = Report(finance_manager.expenses, finance_manager.incomes)
                    report.generate_monthly_report()
                elif option == '5':
                    finance_manager.save_data()
                    break
                else:
                    print("Invalid option. Please try again.")
        else:
            print("Invalid username or password.")

if __name__ == "__main__":
    main()