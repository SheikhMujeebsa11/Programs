n = 4
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    # Increasing part
    for j in range(1, i + 1):
        print(chr(ord('A') + j - 1), end=" ")
    # Decreasing part
    for j in range(i - 1, 0, -1):
        print(chr(ord('A') + j - 1), end=" ")
    print()
