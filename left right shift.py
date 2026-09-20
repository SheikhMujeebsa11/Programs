n = int(input("Enter an integer: "))

left_shift = n << 1
right_shift = n >> 1

print(f"Left shift (n << 1) results in: {left_shift} (Equivalent to {n} * 2)")
print(f"Right shift (n >> 1) results in: {right_shift} (Equivalent to {n} // 2)")
