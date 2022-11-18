from flask import Flask
from flask_restful import Api
from flask.json import JSONEncoder
from bson import json_util
from mongoengine.base import BaseDocument
from mongoengine.queryset.base import BaseQuerySet
from resources.HotelResource import HotelResource
from database.db import initialize_db


class MongoEngineJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, BaseDocument):
            return json_util._json_convert(obj.to_mongo())
        elif isinstance(obj, BaseQuerySet):
            return json_util._json_convert(obj.as_pymongo())
        return JSONEncoder.default(self, obj)


app = Flask(__name__)  # Create an instance of this class.
app.config['MONGODB_SETTINGS'] = {
    'db': 'app-rest',
    'host': 'mongodb://localhost:27017/app-rest'
}
initialize_db(app)
app.json_encoder = MongoEngineJSONEncoder
api = Api(app)  # main entry point of the application. You need to initialize it with a Flask Application object (app)
#
# headers = {'Content-Type': 'application/json'}


#
# @app.route('/api/guests')
# class Guest(Resource):
#     def get(self):
#         get_parser = reqparse.RequestParser()  # From flask library.
#         get_parser.add_argument('id', type=str, location='args', required=True)
#         get_parser.add_argument('f_name', type=str, location='args', required=True)
#         get_parser.add_argument('l_name', type=str, location='args', required=True)
#         get_parser.add_argument('phone', type=int, location='args', required=True)
#         get_parser.add_argument('email', type=str, location='args', required=True)
#         args = get_parser.parse_args()  # Stores value of "id" (and any other query params), defaults to None.
#
#
# @app.route('/api/rooms')
# class Room(Resource):
#     def get(self):
#         get_parser = reqparse.RequestParser()  # From flask library.
#         get_parser.add_argument('hotel_id', type=str, location='args', required=True)
#         get_parser.add_argument('model', type=str, location='args', required=True)
#         get_parser.add_argument('id', type=str, location='args', required=True)
#         get_parser.add_argument('capacity', type=int, location='args', required=True)
#         get_parser.add_argument('price', type=int, location='args', required=True)
#         get_parser.add_argument('img', type=list, location='args', required=False)
#         get_parser.add_argument('rating', type=int, location='args', required=False)
#         args = get_parser.parse_args()  # Stores value of "id" (and any other query params), defaults to None.
#
#
# @app.route('/api/items')
# class Item(Resource):
#     def get(self):
#         get_parser = reqparse.RequestParser()  # From flask library.
#         get_parser.add_argument('hotel_id', type=str, location='args', required=True)
#         get_parser.add_argument('name', type=str, location='args', required=True)
#         get_parser.add_argument('id', type=str, location='args', required=True)
#         get_parser.add_argument('stock', type=int, location='args', required=True)
#         get_parser.add_argument('price', type=int, location='args', required=True)
#         get_parser.add_argument('img', type=list, location='args', required=False)
#         get_parser.add_argument('rating', type=int, location='args', required=False)
#         args = get_parser.parse_args()  # Stores value of "id" (and any other query params), defaults to None.


api.add_resource(HotelResource,
                 '/hotel',
                 '/hotel/',
                 '/hotel/<string:hotel_id>')


@app.route('/')
def hello_world():
    return "Yay! Your web application is running fine!"


if __name__ == '__main__':
    app.run(port=8080)  # Runs web app @ http://localhost:8080.
