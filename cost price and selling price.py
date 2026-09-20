def check_profit_loss():
    cp = float(input("Enter Cost Price: "))
    sp = float(input("Enter Selling Price: "))

    if sp > cp:
        profit = sp - cp
        print(f"Profit of {profit:.2f}")
    elif cp > sp:
        loss = cp - sp
        print(f"Loss of {loss:.2f}")
    else:
        print("No Profit, No Loss.")

check_profit_loss()
