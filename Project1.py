from functools import reduce


def get_expenses():
    expenses = []

    count = int(input("How many monthly expenses would you like to enter? "))

    for i in range(count):
        print(f"\nExpense #{i + 1}")
        name = input("Enter expense type: ")
        amount = float(input("Enter expense amount: "))
        expenses.append((name, amount))

    return expenses


def calculate_total(expenses):
    return reduce(lambda acc, item: acc + item[1], expenses, 0)


def get_highest(expenses):
    return reduce(lambda a, b: a if a[1] > b[1] else b, expenses)


def get_lowest(expenses):
    return reduce(lambda a, b: a if a[1] < b[1] else b, expenses)


def main():
    print("=== Monthly Expense Tracker ===")

    expenses = get_expenses()

    total = calculate_total(expenses)
    highest = get_highest(expenses)
    lowest = get_lowest(expenses)

    print("\n--- Expense Summary ---")
    print(f"Total Expenses: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} (${highest[1]:.2f})")
    print(f"Lowest Expense: {lowest[0]} (${lowest[1]:.2f})")


if __name__ == "__main__":
    main()