number = int(input("Enter an integer: "))

if number % 3 == 0 and number % 5 == 0:
    print(f"{number} is divisible by both 3 and 5")
elif number % 3 == 0:
    print(f"{number} is divisible by 3")
elif number % 5 == 0:
    print(f"{number} is divisible by 5")
else:
    print(f"{number} is divisible by neither 3 nor 5")
