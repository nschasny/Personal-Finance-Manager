class Budget:
    def __init__(self, amount):
        self.amount = amount

    def set_budget(self, amount):
        self.amount = amount

    def get_budget(self):
        return self.amount

    def is_within_budget(self, total_spending):
        return total_spending <= self.amount