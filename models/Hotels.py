from mongoengine import Document, StringField, IntField


class Hotels(Document):
    hotel_id = StringField(max_length=10, required=True)
    # pw = StringField(required=True)
    name = StringField(max_length=100, required=True)
    email = StringField(required=True)
    # street = StringField(max_length=50)
    # city = StringField(max_length=50)
    # state = StringField(max_length=50)
    zip_code = IntField(max_length=10)
    # country = StringField(max_length=50)
    phone = IntField(max_length=10)
