def find_quadrant():
    x = float(input("Enter X coordinate: "))
    y = float(input("Enter Y coordinate: "))

    if x > 0 and y > 0:
        print("The point lies in Quadrant I.")
    elif x < 0 and y > 0:
        print("The point lies in Quadrant II.")
    elif x < 0 and y < 0:
        print("The point lies in Quadrant III.")
    elif x > 0 and y < 0:
        print("The point lies in Quadrant IV.")
    elif x == 0 and y != 0:
        print("The point lies on the Y-axis.")
    elif y == 0 and x != 0:
        print("The point lies on the X-axis.")
    else:
        print("The point is at the Origin (0,0).")

find_quadrant()
