from flask import Flask
from flask_restful import Api
from flask.json import JSONEncoder
from bson import json_util
from mongoengine.base import BaseDocument
from mongoengine.queryset.base import BaseQuerySet
from resources.Hotel import Hotel
from resources.Guest import Guest
from resources.Session import Session
from resources.Item import Item
from resources.Room import Room
from resources.User import User
from resources.Reservation import Reservation
from database.db import initialize_db
from jwt import exceptions as jwt_exception
from flask_jwt_extended import JWTManager

class MongoEngineJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, BaseDocument):
            return json_util._json_convert(obj.to_mongo())
        elif isinstance(obj, BaseQuerySet):
            return json_util._json_convert(obj.as_pymongo())
        return JSONEncoder.default(self, obj)


app = Flask(__name__)  # Create an instance of this class.
app.config['MONGODB_SETTINGS'] = {
    'db': 'app-ezstay',
    'host': 'mongodb://localhost:27017/app-ezstay'
}
app.config['JWT_SECRET_KEY'] = 'idk'  # Change this!
app.config['PROPAGATE_EXCEPTIONS'] = True
initialize_db(app)
jwt = JWTManager(app)
app.json_encoder = MongoEngineJSONEncoder
api = Api(app)  # main entry point of the application. You need to initialize it with a Flask Application object (app)
# headers = {'Content-Type': 'application/json'}


api.add_resource(Hotel,
                 '/hotel',
                 '/hotel/',
                 '/hotel/<string:hotel_id>')

api.add_resource(Guest,
                 '/guest',
                 '/guest/',
                 '/guest/<string:guest_id>')

api.add_resource(Item,
                 '/hotel/<string:hotel_id>/item',
                 '/hotel/<string:hotel_id>/item/<string:pagesize>')

api.add_resource(Room,
                 '/hotel/<string:hotel_id>/room')

api.add_resource(Reservation,
                 '/guest/<string:guest_id>/reservation')

api.add_resource(Session, '/session')

api.add_resource(User, '/user')


@app.route('/')
def hello_world():
    raise jwt_exception.ExpiredSignatureError
    # return "Yay! Your web application is running fine!"


if __name__ == '__main__':
    app.run(port=8080)  # Runs web app @ http://localhost:8080.
