import pickle

class Expense:
    def __init__(self, category, amount, description):
        self.category = category
        self.amount = amount
        self.description = description

class Income:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

class FinanceManager:
    def __init__(self):
        self.expenses = []
        self.incomes = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def add_income(self, income):
        self.incomes.append(income)

    def save_data(self):
        with open('finance_data.pkl', 'wb') as f:
            pickle.dump((self.expenses, self.incomes), f)

    def load_data(self):
        try:
            with open('finance_data.pkl', 'rb') as f:
                self.expenses, self.incomes = pickle.load(f)
        except FileNotFoundError:
            self.expenses, self.incomes = [], []