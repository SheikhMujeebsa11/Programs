number = int(input("Enter an integer: "))
original_number = number
count = 0

# Using Brian Kernighan’s Algorithm to clear the lowest set bit efficiently
while number > 0:
    number = number & (number - 1)
    count += 1

print(f"The number of set bits in {original_number} (binary: {bin(original_number)[2:]}) is: {count}")
