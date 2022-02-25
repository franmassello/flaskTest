
from flask import Flask, jsonify, request, abort
from functions.gcd_euclides import gcd_euclides

from flask_restful import Resource, Api
from marshmallow import Schema, fields

app = Flask(__name__)
app.config["DEBUG"] = True

#class BarQuerySchema(Schema):
#    A = fields.Str(required=True)
#    B = fields.Str(required=True)

app = Flask(__name__)
api = Api(app)
#schema = BarQuerySchema()
port = 5000
class GCD(Resource):
    def get(self):
        resultado_funcion = {"resultado" : gcd_euclides(request.args["A"], request.args["B"])}
        return jsonify(resultado_funcion)

class Test(Resource):
    def get(self):
        objeto_response = {"Resultado" : "OK", "URL" : request.base_url}
        return objeto_response

api.add_resource(Test, "/test")
api.add_resource(GCD, '/gcd', endpoint='gcd')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)








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