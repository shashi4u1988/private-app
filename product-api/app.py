from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Products(Resource):
    def get(self):
        return {'products': [
          "devops",
          "SRE",
          "Development",
          "Databases",
        ]}

api.add_resource(Products, '/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
