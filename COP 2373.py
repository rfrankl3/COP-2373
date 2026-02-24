from functools import reduce

def main():
    print("Monthly Expense Analyzer")
    print("------------------------")

    expenses = []

    count = int(input("How many expenses would you like to enter? "))

    for i in range(count):
        print(f"\nExpense #{i+1}")
        expense_type = input("Enter expense type: ")
        amount = float(input("Enter expense amount: $"))

        expenses.append((expense_type, amount))

    total = reduce(lambda acc, exp: acc + exp[1], expenses, 0)

    highest = reduce(lambda a, b: a if a[1] > b[1] else b, expenses)

    lowest = reduce(lambda a, b: a if a[1] < b[1] else b, expenses)

    print("\nExpense Summary")
    print("----------------")
    print(f"Total Expenses: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} (${highest[1]:.2f})")
    print(f"Lowest Expense: {lowest[0]} (${lowest[1]:.2f})")


main()