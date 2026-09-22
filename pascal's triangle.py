n = 4
for i in range(1, n + 1):
    # Print leading spaces for centering
    print(" " * (n - i), end="")
    val = 1
    for j in range(1, i + 1):
        print(val, end=" ")
        val = val * (i - j) // j
    print()
