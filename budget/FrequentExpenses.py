from . import Expense
import collections

expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')
