class InsufficientBalanceException(Exception):
    def __init__(self, balance, amount):
        message = f"Insufficient balance! Available balance: ${balance}, Amount to withdraw: ${amount}"
        super().__init__(message)

# Define a function to withdraw money
def withdraw_money(balance, amount):
    if amount > balance:
        raise InsufficientBalanceException(balance, amount)
    else:
        new_balance = balance - amount
        print(f"Withdrawal successful! New balance: ${new_balance}")

try:
    balance = 1000
    amount = 1500
    withdraw_money(balance, amount)
except InsufficientBalanceException as e:
    print(f"Error: {e}")
