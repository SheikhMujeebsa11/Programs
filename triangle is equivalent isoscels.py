side1 = float(input("Enter length of side 1: "))
side2 = float(input("Enter length of side 2: "))
side3 = float(input("Enter length of side 3: "))

# First ensure it's a valid triangle structure before classifying
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    if side1 == side2 == side3:
        print("Equilateral Triangle")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("These dimensions cannot form a valid triangle.")
