from mongoengine import Document, StringField, IntField, ListField


class Rooms(Document):
    hotel_id = StringField(max_length=10, required=True)
    model = StringField()
    room_id = StringField(required=True)
    capacity = IntField()
    price = IntField()
    # img = ListField()
    # rating = IntField()
