import uuid
from models.Reservations import Reservations


def get_reservations_by_guest(guest_id: str):
    reservations = None
    if guest_id is not None:
        reservations = Reservations.objects(guest_id=guest_id)
    return reservations


def create_reservation(guest_id: str, hotel_id: str, room_id: str, start_date: str, end_date: str):
    while True:
        gen_reservation_id = str(uuid.uuid4())[0:7]
        if len(Reservations.objects(room_id=gen_reservation_id)) == 0:
            break
    reservation_doc = Reservations(guest_id=guest_id,
                                   reservation_id=gen_reservation_id,
                                   hotel_id=hotel_id,
                                   room_id=room_id,
                                   start_date=start_date,
                                   end_date=end_date
                                   )
    reservation_doc.save()
    return reservation_doc
