def gcd_euclides(a, b):
    if type(a) != int or type(b) != int:
        return "Error: los valores deben ser enteros"
    else:
        int(a)
        int(b)
        if b == 0:
            return a
        else:
            return gcd_euclides(b, a % b)
