from mongoengine import Document, StringField, IntField

class Guests(Document):
    id = StringField()
    f_name = StringField()
    l_name = StringField()
    phone = IntField()
    email = StringField()