from flask import Flask, request
from flask_restful import abort, Api, Resource

app = Flask(__name__)
api = Api(app)

vector = [1, 2, 3, 4, 5]


class RecObj(Resource):
    def get(self):
        return vector

    def post(self):
        vector.append(int(request.json["num"]))
        return f"El número adjuntado fue: {request.json['num']}"


class RecObjEsp(Resource):
    def get(self, id):
        return vector[id]

    def put(self, id):
        value = int(request.json["value"])
        vector[id] = value
        return f"El número cambiado fue: {request.json['value']} en la posición {id}"


api.add_resource(RecObj, '/test')
api.add_resource(RecObjEsp, '/test/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
