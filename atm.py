def atm_withdrawal():
    balance = 50000.0  # Dummy current balance
    min_balance = 1000.0  # Minimum operational balance required

    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Invalid amount. Please enter a value greater than zero.")
    elif amount > balance:
        print("Transaction Rejected: Insufficient balance.")
    elif (balance - amount) < min_balance:
        print(f"Transaction Rejected: Retaining less than the required minimum balance of ₹{min_balance}.")
    else:
        balance -= amount
        print("Transaction Approved!")
        print(f"Please collect your cash. Remaining Balance: ₹{balance:.2f}")

atm_withdrawal()
