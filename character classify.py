char = input("Enter a single character: ")

if len(char) != 1:
    print("Please enter exactly one character.")
else:
    if char.isupper():
        print(f"'{char}' is an Uppercase alphabet")
    elif char.islower():
        print(f"'{char}' is a Lowercase alphabet")
    elif char.isdigit():
        print(f"'{char}' is a Digit")
    else:
        print(f"'{char}' is a Special Character")
