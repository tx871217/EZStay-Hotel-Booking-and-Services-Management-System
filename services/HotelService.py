from models.Hotels import Hotels


def get_hotel(hotel_id: str):  # Service for the GET() method
    if hotel_id is None:
        hotel_doc = Hotels.objects()  # Returning a list of all objects
    else:
        hotel_doc = Hotels.objects(id=hotel_id)  # Returning a list of all objects that match the specific id
    return hotel_doc


def create_hotel(name: str, email: str, zip_code: int, phone: int):  # Service for the POST() method
    hotel_doc = Hotels(name=name,
                       email=email,
                       zip_code=zip_code,
                       phone=phone
                       )  # Create a new rider object
    hotel_doc.save()  # Save the newly created rider object to the db
    return hotel_doc  # Return the list of one rider object that was created


def update_hotel(hotel_id: str, name: str, email: str, zip_code: int, phone: int):  # Service for the PATCH() method
    hotel_doc = Hotels.objects(id=hotel_id).first()  # extracting the first object from a list of one object
    hotel_doc.update(name=name)
    hotel_doc.update(email=email)
    hotel_doc.update(zip_code=zip_code)
    hotel_doc.update(phone=phone)
    hotel_doc.reload()  # Get the latest copy from the db
    return hotel_doc  # Return the list of one rider object that was updated
