from flask_restful import reqparse, Resource
from flask import make_response  # returns an HTML response
from services.HotelService import *
from services.ItemService import *

post_parser = reqparse.RequestParser()
post_parser.add_argument('name', type=str, default="")
post_parser.add_argument('price', type=int, default=0)
post_parser.add_argument('stock', type=int, default=0)

headers = {'Content-Type': 'application/json'}


class Item(Resource):
    def get(self, hotel_id):
        # hotel = get_hotel_by_id(hotel_id)
        items = get_items_by_hotel(hotel_id)
        return make_response(items.to_json(), 200, headers)

    def post(self, hotel_id):
        # hotel = get_hotel(hotel_id)
        args = post_parser.parse_args()
        # if len(args.name) or len(args.price) or len(args.stock) == 0:
        #     return "ERROR! item's name, price, stock are required.", 400
        # else:
        item_doc = create_item_by_hotel(hotel_id, args.name, args.price, args.stock)
        return make_response(item_doc.to_json(), 200, headers)