import . from Expense
import collections

expense = Expense.Expenses()
expenses.read_expense('data/spending_data.csv')
spending_categories = []
    for expense in expenses.list:
        spending_categories.append(expense.category)

spending_counter = collections.Counter(spending_categories)
print(spending_counter)
