from mongoengine import Document, StringField


class Users(Document):
    email = StringField(max_length=100, required=True)
    password_hash = StringField(required=True)