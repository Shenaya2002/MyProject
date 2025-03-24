def check_balance(balance):
    """Displays the current account balance."""
    print("\nExecuting: check_balance()")
    print(f"Your current balance is: ${balance:.2f}")

def deposit(balance, amount):
    """Deposits money into the account."""
    print("\nExecuting: deposit()")
    if amount > 0:
        balance += amount
        print(f"${amount:.2f} deposited successfully!")
    else:
        print("Deposit amount must be greater than zero.")
    return balance
