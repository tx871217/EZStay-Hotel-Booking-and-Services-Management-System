from models.Hotels import Hotels
import uuid
from utils import get_hash


# default_hotels = {'abc@123.com': 'xyz'}

def get_hotel(hotel_id: str):  # Service for the GET() method
    if hotel_id is None:
        hotel_doc = Hotels.objects()  # Returning a list of all objects
    else:
        hotel_doc = Hotels.objects(hotel_id=hotel_id)  # Returning a list of all objects that match the specific id
    return hotel_doc


# def init_hotels():
#     existing_hotels = Hotels.objects()
#     if len(existing_hotels) == 0:
#         for hotel_email in default_hotels:
#             pw = get_hash(default_hotels[hotel_email].encode('utf-8'))
#             create_hotel(hotel_email, pw)
def get_hotel_by_id(hotel_id: str):
    hotel_doc = None
    if hotel_id is not None:
        hotel_doc = Hotels.objects(hotel_id=hotel_id).first()
    return hotel_doc


def get_hotel_by_email(email: str):  # Service for the GET() method
    hotel_doc = None
    if email is not None:
        hotel_doc = Hotels.objects(email=email).first()  # Returning the only object that matches the specific email
    return hotel_doc


def create_hotel(name: str, email: str, zip_code: int, phone: int):  # Service for the POST() method
    while True:
        gen_hotel_id = str(uuid.uuid4())[0:7]
        if len(Hotels.objects(hotel_id=gen_hotel_id)) == 0:
            break
    hotel_doc = Hotels(hotel_id=gen_hotel_id,
                       name=name,
                       email=email,
                       zip_code=zip_code,
                       phone=phone
                       )  # Create a new rider object
    hotel_doc.save()  # Save the newly created rider object to the db
    return hotel_doc  # Return the list of one rider object that was created


def update_hotel(hotel_id: str, name: str, email: str, zip_code: int, phone: int):  # Service for the PATCH() method
    hotel_doc = Hotels.objects(hotel_id=hotel_id).first()  # extracting the first object from a list of one object
    hotel_doc.update(name=name)
    hotel_doc.update(email=email)
    hotel_doc.update(zip_code=zip_code)
    hotel_doc.update(phone=phone)
    hotel_doc.reload()  # Get the latest copy from the db
    return hotel_doc  # Return the list of one rider object that was updated


def delete_hotel(hotel_id: str):
    Hotels.objects(hotel_id=hotel_id).first().delete()
