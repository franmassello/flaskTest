# pip install Flask 
# run 
from flask import Flask, jsonify, request
app = Flask(__name__)
app.config["DEBUG"] = True

def gcd_euclides(a, b):
    if b == 0:
        return a
    else:
        return gcd_euclides(b, a % b)

@app.route('/', methods=['GET'])
def home():
    variableTest = "Hello World"
    return variableTest

@app.route('/gcd', methods=['GET'])
def gcd():
    variableA = int(request.args.get('a'))
    variableB = int(request.args.get('b'))
    variableResult = gcd_euclides(variableA, variableB)
    return jsonify(variableResult)
    
app.run()