n = 4
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j % 2 == 1:
            print("0", end=" ")
        else:
            print("1", end=" ")
    print()
