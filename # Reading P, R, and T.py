# Reading P, R, and T
p = float(input("Enter Principal amount: "))
r = float(input("Enter Rate of interest (%): "))
t = float(input("Enter Time period (years): "))

# Calculating Simple Interest
simple_interest = (p * r * t) / 100

print(f"Simple Interest is: {simple_interest:.2f}")
