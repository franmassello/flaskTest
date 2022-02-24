# pip install Flask 
# run 
from flask import Flask, jsonify, request
from functions.gcd_euclides import gcd_euclides

app = Flask(__name__)
app.config["DEBUG"] = True

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