# Hour format expected: 0 to 23
hour = int(input("Enter hour (0-23): "))

if 0 <= hour < 5 or 22 <= hour <= 23:
    print("Night")
elif 5 <= hour < 12:
    print("Morning")
elif 12 <= hour < 17:
    print("Afternoon")
elif 17 <= hour < 22:
    print("Evening")
else:
    print("Invalid hour code entered!")
