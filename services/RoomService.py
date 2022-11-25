from models.Rooms import Rooms
import uuid


def get_rooms_by_hotel(hotel_id: str):
    rooms = None
    if hotel_id is not None:
        rooms = Rooms.objects(hotel_id=hotel_id)
    return rooms


def create_room_by_hotel(hotel_id: str, model: str, price: int, capacity: int):
    while True:
        gen_room_id = str(uuid.uuid4())[0:7]
        if len(Rooms.objects(room_id=gen_room_id)) == 0:
            break
    room_doc = Rooms(hotel_id=hotel_id,
                     room_id=gen_room_id,
                     capacity=capacity,
                     price=price,
                     model=model
                     )
    room_doc.save()
    return room_doc
