from mongoengine import Document, StringField, IntField, ListField


class Items(Document):
    hotel_id = StringField(max_length=10, required=True)
    name = StringField(required=True)
    item_id = StringField(max_length=10, required=True)
    stock = IntField()
    price = IntField()
    # img = ListField()
    # rating = IntField()
