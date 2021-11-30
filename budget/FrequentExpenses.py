from . import Expense
import collections

import matplotlib.pyplot as plt # Remember need to pip install matplotlib

expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')
spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)

spending_counter = collections.Counter(spending_categories)
top5 = spending_counter.most_common(5)
categories, count = zip(*top5)


# Graph each spending category count as a bar chart
fix, ax - plt.subplots()
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')
plt.show()
