from models.Items import Items
import uuid


def get_items_by_hotel(hotel_id: str):
    items = None
    if hotel_id is not None:
        items = Items.objects(hotel_id=hotel_id)
    return items


def create_item_by_hotel(hotel_id: str, name: str, price: int, stock: int):
    while True:
        gen_item_id = str(uuid.uuid4())[0:7]
        if len(Items.objects(item_id=gen_item_id)) == 0:
            break
    item_doc = Items(hotel_id=hotel_id,
                     item_id=gen_item_id,
                     stock=stock,
                     price=price,
                     name=name
                     )
    item_doc.save()
    return item_doc
