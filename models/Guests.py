from mongoengine import Document, StringField, IntField


class Guests(Document):
    guest_id = StringField(max_length=10, required=True)
    f_name = StringField()
    l_name = StringField()
    phone = IntField()
    email = StringField()
