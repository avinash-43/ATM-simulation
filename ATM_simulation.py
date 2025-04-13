def verify_pin(pin):
    """Verify the user by checking their PIN."""
    return input("Enter PIN: ") == pin

def check_balance(balance):
    """Display the current balance."""
    print("Balance: " + str(balance))

def deposit(balance):
    """Deposit an amount into the balance."""
    amt = int(input("Deposit: "))
    balance = balance + amt
    print("Deposited.")
    return balance

def withdraw(balance):
    """Withdraw an amount from the balance if sufficient balance exists."""
    amt = int(input("Withdraw: "))
    if amt <= balance:
        balance = balance - amt
        print("Withdrawn.")
    else:
        print("Insufficient balance.")
    return balance

def change_pin(pin):
    "Change the current PIN."
    pin = input("New PIN: ")
    print("PIN changed.")
    return pin

def atm():
    "Main function to run the ATM."
    balance = 5000
    pin = "1526"

    if not verify_pin(pin):
        print("Wrong PIN!")
        return

    while True:
        print("\n1. Check Balance  2. Deposit  3. Withdraw  4. Change PIN  5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            pin = change_pin(pin)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

atm()
