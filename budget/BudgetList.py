
class BudgetList():
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []

    #def append(self, item):
    # implement append so that it only appends to self if total < budget
    def append(self, item):
        if (self.sum_expenses < self.budget):
            self.expenses.append(item)
            self.sum_expenses += item
            # Otherwise append to the overages list and add to the overage total
        else:
            self.overages.append(item)
            self.sum_overages+=item 
