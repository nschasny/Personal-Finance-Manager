import matplotlib.pyplot as plt
import pandas as pd

class Report:
    def __init__(self, expenses, incomes):
        self.expenses = expenses
        self.incomes = incomes

    def generate_monthly_report(self):
        expense_data = {'Category': [e.category for e in self.expenses], 'Amount': [e.amount for e in self.expenses]}
        income_data = {'Category': [i.category for i in self.incomes], 'Amount': [i.amount for i in self.incomes]}

        df_expenses = pd.DataFrame(expense_data)
        df_incomes = pd.DataFrame(income_data)

        total_expenses = df_expenses['Amount'].sum()
        total_income = df_incomes['Amount'].sum()

        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Net Savings: ${total_income - total_expenses:.2f}")

        df_expenses.plot(kind='bar', x='Category', y='Amount', title='Expenses by Category')
        plt.show()
        
        df_incomes.plot(kind='bar', x='Category', y='Amount', title='Income by Category')
        plt.show()