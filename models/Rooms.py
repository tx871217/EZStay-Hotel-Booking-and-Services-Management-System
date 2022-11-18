from mongoengine import Document, StringField, IntField, ListField

class Rooms(Document):
    hotel_id = StringField()
    model = StringField()
    id = StringField()
    capacity = IntField()
    price = IntField()
    img = ListField()
    rating = IntField()