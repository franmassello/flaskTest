
from flask import Flask, jsonify, request, abort
from functions.gcd_euclides import gcd_euclides

from flask_restful import Resource, Api
from marshmallow import Schema, fields

app = Flask(__name__)
app.config["DEBUG"] = True

class BarQuerySchema(Schema):
    A = fields.Str(required=True)
    B = fields.Str(required=True)

app = Flask(__name__)
api = Api(app)
schema = BarQuerySchema()

class GCD(Resource):
    def get(self):
        errors = schema.validate(request.args)
        if errors:
            abort(400, str(errors))
        return jsonify(gcd_euclides(request.args["A"], request.args["B"]))

api.add_resource(GCD, '/gcd', endpoint='gcd')

if __name__ == '__main__':
    app.run(debug=True)








"""
Diseño en flask puro sin flask-restful
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
    
app.run() """