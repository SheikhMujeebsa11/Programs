ch = input("Enter an alphabet character: ").lower()

if len(ch) == 1 and ch.isalpha():
    if ch in ['a', 'e', 'i', 'o', 'u']:
        print(f"'{ch}' is a Vowel")
    else:
        print(f"'{ch}' is a Consonant")
else:
    print("Please enter a single valid alphabet letter.")
