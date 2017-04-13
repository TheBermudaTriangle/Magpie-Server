import json
import os
from flask import Flask
from flask import request, jsonify
from flask_restful import Resource, Api, reqparse, abort
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)
api = Api(app)

client = MongoClient(os.environ['MONGODB_URI'])
db = client.heroku_qqx020h6
collection = db.userinfo
#posts = db.posts
#post = {'username':'nit','lat':29.951573,'lng':76.815305}

mylist = []
mylist = [{'username':'nit','lat':29.951573,'lng':76.815305},{'username':'singhal','lat':26.830996,'lng':75.762118},{'username':'swapnil','lat':25.5794912,'lng':85.1167952},{'username':'bhatiya','lat':28.3953089,'lng':77.2698073}]

class TodoList(Resource):
    def get(self):
        cursor = collection.find()
        x = dumps(cursor)
        #print(type(x))
        y = json.loads(x)
        #print(type(y))
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
        print(user_name)  
        document = {'username':user_name, 'lat':lat, 'lng':lng}
        collection.delete_one({'username':user_name,'lat':lat,'lng':lng})
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