def find_factorial(n):
    if n < 0: return "Undefined"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
