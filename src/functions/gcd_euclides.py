def gcd_euclides(a, b):
    if b == 0:
        return a
    else:
        return gcd_euclides(b, a % b)
