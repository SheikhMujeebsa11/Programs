import math

def quadratic_roots():
    print("For equation: ax^2 + bx + c = 0")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    if a == 0:
        print("Coefficient 'a' cannot be zero in a quadratic equation.")
        return

    # Calculate discriminant
    d = (b ** 2) - (4 * a * c)

    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        print("The roots are Real and Distinct.")
        print(f"Root 1 = {root1:.2f}")
        print(f"Root 2 = {root2:.2f}")
    elif d == 0:
        root1 = -b / (2 * a)
        print("The roots are Real and Equal.")
        print(f"Root 1 = Root 2 = {root1:.2f}")
    else:
        real_part = -b / (2 * a)
        imag_part = math.sqrt(-d) / (2 * a)
        print("The roots are Imaginary.")
        print(f"Root 1 = {real_part:.2f} + {imag_part:.2f}i")
        print(f"Root 2 = {real_part:.2f} - {imag_part:.2f}i")

quadratic_roots()
