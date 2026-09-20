age = int(input("Enter age: "))

# Dynamic ticket pricing rules
if age < 5:
    price = 0  # Free for toddlers
elif age <= 12:
    price = 10  # Child rate
elif age <= 60:
    price = 20  # Adult rate
else:
    price = 15  # Senior discount

print(f"Ticket Price: ${price}")
