from mongoengine import Document, StringField, IntField

class Reservations(Document):
    guest_id = StringField(max_length=10, required=True)
    hotel_id = StringField(max_length=10, required=True)
    room_id = StringField(max_length=10, required=True)
    start_date = StringField(required=True)
    end_date = StringField(required=True)
    reservation_id = StringField(max_length=10, required=True)