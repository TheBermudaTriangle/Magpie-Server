import json
import os
from flask import Flask
from flask import request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

mylist = []

mylist = [{username:'nit',lat:29.951573,lng:76.815305},{username:'singhal',lat:26.830996,lng:75.762118},{username:'swapnil',lat:25.5794912,lng:85.1167952},{username:'bhatiya',lat:28.3953089,lng:77.2698073}]
class TodoList(Resource):
    def get(self):
        return {"data":mylist}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('lat')
        parser.add_argument('lng')
        args = parser.parse_args()
        lat = args['lat']
        lon = args['lng']
        myDict[]
        return {"data":mylist}

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, port=port, host='0.0.0.0')
