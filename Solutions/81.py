# Dalip's Approach
balance = 0
print("Welcome to the Bank Transaction Log!")
print("Type 'D' for Deposit, Type 'W' for Withdraw or 'exit' to quit.")

while True:
    user = input("Enter your choice (D/W/exit): ").lower()
    if user == "d":
        print(f"Current Balance: {balance}")
        amount = int(input("Enter amount to Deposit: "))
        if amount > 0:
            balance += amounts
            print(f"Deposited {amount}. New Balance: {balance}")
        else:
            print("Deposit amount must be Positive!")
    elif user == "w":
        print(f"Current Balance: {balance}")
        amount = int(input("Enter amount to Withdraw: "))
        if amount <= 0:
            print("Withdrawal must be positive!")
        elif amount > balance:
            print("Insufficient balance! Transaction cancelled")
        else:
            balance -= amount
            print(f"Withdrew {amount}. New Balance: {balance}")

    elif user == "exit":
        print("Exiting Transaction Log...")
        break
    else:
        print("Invalid input! Please Enter 'D','W', or 'exit'.")
print(f"\nFinal Balance (Net Amount): {balance}")
