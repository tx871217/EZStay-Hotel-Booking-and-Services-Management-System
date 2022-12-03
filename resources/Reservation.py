from flask_restful import reqparse, Resource
from flask import make_response, abort  # returns an HTML response
from services.ReservationService import *

from flask_jwt_extended import jwt_required, get_jwt_identity

post_parser = reqparse.RequestParser()
post_parser.add_argument('hotel_id', type=str, default="")
post_parser.add_argument('room_id', type=str, default="")
post_parser.add_argument('start_date', type=str, default="")
post_parser.add_argument('end_date', type=str, default="")

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('start_date', type=str, default="")
patch_parser.add_argument('end_date', type=str, default="")

headers = {'Content-Type': 'application/json'}

class Reservation(Resource):
    def get(self, guest_id):
        reservations = get_reservations_by_guest(guest_id)
        return make_response(reservations.to_json(), 200, headers)

    def post(self, guest_id):
        # hotel = get_hotel(hotel_id)
        args = post_parser.parse_args()
        # if len(args.name) or len(args.price) or len(args.stock) == 0:
        #     return "ERROR! item's name, price, stock are required.", 400
        # else:
        reservation_doc = create_reservation(guest_id, args.hotel_id, args.room_id, args.start_date, args.end_date)
        return make_response(reservation_doc.to_json(), 200, headers)