a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

print(f"Before swapping: a = {a}, b = {b}")

# Swapping logic using XOR
a = a ^ b
b = a ^ b
a = a ^ b

print(f"After swapping: a = {a}, b = {b}")
