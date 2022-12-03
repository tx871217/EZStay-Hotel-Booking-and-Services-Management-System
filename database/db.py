from flask_mongoengine import MongoEngine
from services.UserService import init_users
from services.HotelService import init_hotels

db = MongoEngine()


def initialize_db(app):
    db.init_app(app)  # Create the db
    init_users()
    init_hotels()


def fetch_engine():
    return db
