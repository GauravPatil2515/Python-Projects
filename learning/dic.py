# # id = { 133:43 , 213:32, 422:43}
# # id2 ={ 213:32, 326:45}
# # print(id)

# # # id.clear()
# # id.popitem()
# # print(id)
# # # del id

# # # print(id)

# # del id[133]

# for i in range(19):
#     print(i)
#     if i==12:
#         break
# else:
#     print("sorry no i")

# i = 0
# while i<12:
#     print(i)
#     i = i + 1
#     if i == 8:
#         # break
#         print("no")


class Expense:
    def __init__(self, amount, category, description, date):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

class PersonalFinanceManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description, date):
        expense = Expense(amount, category, description, date)
        self.expenses.append(expense)

    def get_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def get_expenses_by_category(self):
        expenses_by_category = {}
        for expense in self.expenses:
            if expense.category in expenses_by_category:
                expenses_by_category[expense.category] += expense.amount
            else:
                expenses_by_category[expense.category] = expense.amount
        return expenses_by_category

# Example usage
if __name__ == "__main__":
    pfm = PersonalFinanceManager()
    pfm.add_expense(50, "Food", "Lunch", "2024-03-10")
    pfm.add_expense(30, "Transportation", "Bus fare", "2024-03-10")
    pfm.add_expense(100, "Shopping", "Clothes", "2024-03-11")

    total_expenses = pfm.get_total_expenses()
    print(f"Total expenses: ${total_expenses}")

    expenses_by_category = pfm.get_expenses_by_category()
    print("Expenses by category:")
    for category, amount in expenses_by_category.items():
        print(f"{category}: ${amount}")
