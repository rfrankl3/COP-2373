# Import reduce from functools
from functools import reduce

def main():
    print("Monthly Expense Analyzer")
    print("------------------------")

    expenses = []  # list to store (type, amount)

    # Ask user how many expenses they want to enter
    count = int(input("How many expenses would you like to enter? "))

    # Input loop
    for i in range(count):
        print(f"\nExpense #{i+1}")
        expense_type = input("Enter expense type: ")
        amount = float(input("Enter expense amount: $"))

        # Store as tuple (type, amount)
        expenses.append((expense_type, amount))

    # Use reduce to calculate total expense
    total = reduce(lambda acc, exp: acc + exp[1], expenses, 0)

    # Use reduce to find highest expense
    highest = reduce(lambda a, b: a if a[1] > b[1] else b, expenses)

    # Use reduce to find lowest expense
    lowest = reduce(lambda a, b: a if a[1] < b[1] else b, expenses)

    # Display results
    print("\nExpense Summary")
    print("----------------")
    print(f"Total Expenses: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} (${highest[1]:.2f})")
    print(f"Lowest Expense: {lowest[0]} (${lowest[1]:.2f})")


# Run the program
main()