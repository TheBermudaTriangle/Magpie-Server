import json
import os
from flask import Flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api, reqparse, abort
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)
CORS(app)
api = Api(app)

client = MongoClient(os.environ['MONGODB_URI'])
db = client.heroku_qqx020h6
collection = db.userinfo

class TodoList(Resource):
    def get(self):
        cursor = collection.find()
        x = dumps(cursor)
        y = json.loads(x)
        return y

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username');
        parser.add_argument('lat')
        parser.add_argument('lng')
        args = parser.parse_args()
        user_name = args['username']
        lat = args['lat']
        lng = args['lng']  
        document = {'username':user_name, 'lat':lat, 'lng':lng}
        collection.delete_one({'username':user_name})
        collection.insert_one(document)
        x = dumps(collection.find())
        y = json.loads(x)
        return y

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username')
        parser.add_argument('lat')
        parser.add_argument('lng')
        args = parser.parse_args()
        user_name = args['username']
        lat = args['lat']
        lng = args['lng']
        parser.parse_args()
        collection.delete_one({'username':user_name,'lat':lat,'lng':lng})

api.add_resource(TodoList, '/')
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, port=port, host='0.0.0.0')