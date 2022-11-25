from flask_mongoengine import MongoEngine

# from services.HotelService import init_hotels

db = MongoEngine()


def initialize_db(app):
    db.init_app(app)  # Create the db
    # init_hotels()
    # init_riders()  # Populate it with default riders


def fetch_engine():
    return db
