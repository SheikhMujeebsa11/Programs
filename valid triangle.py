a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = float(input("Enter side C: "))

# Triangle Inequality Theorem: Sum of any two sides must be strictly greater than the third side
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Valid Triangle: A triangle can be formed with these side lengths.")
else:
    print("Invalid Triangle: The sum of two sides must be greater than the third side.")
