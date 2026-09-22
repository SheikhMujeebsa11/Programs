n = 4
# Top half + center line
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1): print(j, end=" ")
    for j in range(i - 1, 0, -1): print(j, end=" ")
    print()
# Bottom half
for i in range(n - 1, 0, -1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1): print(j, end=" ")
    for j in range(i - 1, 0, -1): print(j, end=" ")
    print()
