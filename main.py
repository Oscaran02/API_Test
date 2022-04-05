from flask import Flask, request
from flask_restful import abort, Api, Resource

app = Flask(__name__)
api = Api(app)

vector = [1, 2, 3, 4, 5]
class RecObj(Resource):
    def get(self):
        return vector

    def post(self):
        print (request.json)
        vector.append(int(request.json["num"]))
        return f"El número adjuntado fue: {request.json['num']}"


class RecObjEsp(Resource):
    def get(self, numero):
        pass

    def post(self):
        pass


api.add_resource(RecObj, '/test')
api.add_resource(RecObjEsp, '/test/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
