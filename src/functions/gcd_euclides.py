from flask import abort, jsonify

def gcd_euclides(a, b):
    try:
        conversionA = int(a)
        conversionB = int(b)
    except ValueError:
        return abort(400, "Error! los valores deben ser enteros")

    if type(conversionA) == int and type(conversionB) == int:
        if conversionB == 0:
            return conversionA
        else:
            return gcd_euclides(conversionB, conversionA % conversionB)
    else: 
        return abort(400, "Error! los valores deben ser enteros")