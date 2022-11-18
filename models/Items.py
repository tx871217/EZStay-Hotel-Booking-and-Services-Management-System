from mongoengine import Document, StringField, IntField, ListField

class Items(Document):
    hotel_id = StringField()
    name = StringField()
    id = StringField()
    stock = IntField()
    price = IntField()
    img = ListField()
    rating = IntField()
