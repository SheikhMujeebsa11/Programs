number = int(input("Enter the number: "))
k = int(input("Enter the bit position K (0-indexed from right): "))

# Creating a mask by shifting 1 left by K positions
mask = 1 << k

if (number & mask) != 0:
    print(f"The {k}-th bit of {number} is SET (1)")
else:
    print(f"The {k}-th bit of {number} is NOT SET (0)")
