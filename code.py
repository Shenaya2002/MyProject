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

def withdraw(balance, amount):
    """Withdraws money from the account if there are sufficient funds."""
    print("\nExecuting: withdraw()")
    if 0 < amount <= balance:
        balance -= amount
        print(f"${amount:.2f} withdrawn successfully!")
    else:
        print("Insufficient funds or invalid amount.")
    return balance

# Main program
balance = 1000.0  # Initial balance

while True:
    print("\nSimple Banking System")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    print("\nExecuting: main program loop")  # Print current execution step

    if choice == "1":
        check_balance(balance)
    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        balance = deposit(balance, amount)
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))
        balance = withdraw(balance, amount)
    elif choice == "4":
        print("\nExecuting: exit program")
        print("Thank you for using our banking system!")
        break
    else:
        print("\nExecuting: invalid choice handler")
        print("Invalid choice! Please try again.")
