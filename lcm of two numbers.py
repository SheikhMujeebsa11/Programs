def find_lcm(a, b):
    if a == 0 or b == 0: return 0
    return abs(a * b) // find_gcd(a, b)
