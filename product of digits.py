def product_of_digits_recursive(n):
    n = abs(n)
    if n < 10:
        return n
    return (n % 10) * product_of_digits_recursive(n // 10)
