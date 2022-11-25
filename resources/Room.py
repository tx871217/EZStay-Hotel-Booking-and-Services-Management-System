from flask_restful import reqparse, Resource
from flask import make_response  # returns an HTML response
from services.HotelService import *
from services.RoomService import *

post_parser = reqparse.RequestParser()
post_parser.add_argument('model', type=str, default="")
post_parser.add_argument('price', type=int, default=0)
post_parser.add_argument('capacity', type=int, default=0)

headers = {'Content-Type': 'application/json'}


class Room(Resource):
    def get(self, hotel_id):
        # hotel = get_hotel_by_id(hotel_id)
        rooms = get_rooms_by_hotel(hotel_id)
        return make_response(rooms.to_json(), 200, headers)

    def post(self, hotel_id):
        # hotel = get_hotel(hotel_id)
        args = post_parser.parse_args()
        # if len(args.name) or len(args.price) or len(args.stock) == 0:
        #     return "ERROR! room's name, price, stock are required.", 400
        # else:
        room_doc = create_room_by_hotel(hotel_id, args.model, args.capacity, args.price)
        return make_response(room_doc.to_json(), 200, headers)