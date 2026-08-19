class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Account Balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Account Balance: ${self.balance:.2f}")
        else:
            print("Withdrawal amount must be positive and cannot exceed the balance.")

    def get_balance(self):
        return self.balance


# Example usage:
if __name__ == "__main__":
    # Create a bank account with an initial balance of $1000
    account = BankAccount(1000)
    
    # Deposit $500
    account.deposit(500)   # Output: Account Balance: $1500.00
    
    # Withdraw $200
    account.withdraw(200)   # Output: Account Balance: $1300.00
    
    # Attempt to withdraw $1500 (should fail)
    account.withdraw(1500)  # Output: Withdrawal amount must be positive and cannot exceed the balance.

    # Deposit $300
    account.deposit(300)     # Output: Account Balance: $1600.00

    # Get the current balance
    print(f"Current Balance: ${account.get_balance():.2f}")  # Output: Current Balance: $1600.00
