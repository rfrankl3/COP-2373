class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = float(amount)
        self.interest_rate = float(interest_rate)

    def adjust_interest_rate(self, new_rate):
        self.interest_rate = float(new_rate)

    def deposit(self, amount):
        if amount > 0:
            self.amount += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.amount:
            self.amount -= amount
            return True
        return False

    def get_balance(self):
        return self.amount

    def calculate_interest(self, days):
        # Simple interest formula: Interest = Principal * Rate * Time
        # Time is in years, so convert days to years
        interest = self.amount * self.interest_rate * (days / 365)
        return interest

    def __str__(self):
        return (
            f"Account Holder: {self.name}\n"
            f"Account Number: {self.account_number}\n"
            f"Balance: ${self.amount:.2f}\n"
            f"Interest Rate: {self.interest_rate:.2%}"
        )


def test_bank_account():
    print("=== Creating Account ===")
    acct = BankAcct("Jim Jones", "123456", 1000.00, 0.05)
    print(acct)

    print("\n=== Deposit Test ===")
    acct.deposit(500)
    print(f"After deposit: ${acct.get_balance():.2f}")

    print("\n=== Withdraw Test ===")
    acct.withdraw(200)
    print(f"After withdrawal: ${acct.get_balance():.2f}")

    print("\n=== Adjust Interest Rate ===")
    acct.adjust_interest_rate(0.03)
    print(f"New interest rate: {acct.interest_rate:.2%}")

    print("\n=== Interest Calculation (30 days) ===")
    interest = acct.calculate_interest(30)
    print(f"Interest for 30 days: ${interest:.2f}")

    print("\n=== Final Account Info ===")
    print(acct)


if __name__ == "__main__":
    test_bank_account()