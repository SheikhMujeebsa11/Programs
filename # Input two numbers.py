# Input two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calculations
sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2

# Handle division by zero edge case safely
if num2 != 0:
    quotient = num1 / num2
    remainder = num1 % num2
else:
    quotient = "Undefined (cannot divide by zero)"
    remainder = "Undefined (cannot divide by zero)"

# Output
print(f"Sum: {sum_result}")
print(f"Difference: {diff_result}")
print(f"Product: {prod_result}")
print(f"Quotient: {quotient}")
print(f"Remainder: {remainder}")
