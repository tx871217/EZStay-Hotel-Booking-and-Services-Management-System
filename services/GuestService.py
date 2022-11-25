from models.Guests import Guests
import uuid


def get_guest(guest_id: str):  # Service for the GET() method
    if guest_id is None:
        guest_doc = Guests.objects()  # Returning a list of all objects
    else:
        guest_doc = Guests.objects(guest_id=guest_id)  # Returning a list of all objects that match the specific id
    return guest_doc


def get_guest_by_id(guest_id: str):
    guest_doc = None
    if guest_id is not None:
        guest_doc = Guests.objects(guest_id=guest_id).first()
    return guest_doc


def create_guest(f_name: str, l_name: str, email: str, phone: int):  # Service for the POST() method
    while True:
        gen_guest_id = str(uuid.uuid4())[0:7]
        if len(Guests.objects(guest_id=gen_guest_id)) == 0:
            break
    guest_doc = Guests(guest_id=gen_guest_id,
                       f_name=f_name,
                       l_name=l_name,
                       email=email,
                       phone=phone
                       )  # Create a new rider object
    guest_doc.save()  # Save the newly created rider object to the db
    return guest_doc  # Return the list of one rider object that was created


def update_guest(guest_id: str, f_name: str, l_name: str, email: str, phone: int):  # Service for the PATCH() method
    guest_doc = Guests.objects(guest_id=guest_id).first()  # extracting the first object from a list of one object
    guest_doc.update(f_name=f_name)
    guest_doc.update(l_name=l_name)
    guest_doc.update(email=email)
    guest_doc.update(phone=phone)
    guest_doc.reload()  # Get the latest copy from the db
    return guest_doc  # Return the list of one rider object that was updated


def delete_guest(guest_id: str):
    Guests.objects(guest_id=guest_id).first().delete()
