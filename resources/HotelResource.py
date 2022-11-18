from flask_restful import reqparse, Resource
from flask import make_response  # returns an HTML response
from services.HotelService import *

post_parser = reqparse.RequestParser()
# post_parser.add_argument('id', type=str)
post_parser.add_argument('name', type=str)
post_parser.add_argument('email', type=str)
post_parser.add_argument('zip_code', type=int)
post_parser.add_argument('phone', type=int)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('name', type=str)
patch_parser.add_argument('email', type=str)
patch_parser.add_argument('zip_code', type=int)
patch_parser.add_argument('phone', type=int)

headers = {'Content-Type': 'application/json'}


class HotelResource(Resource):
    def get(self, hotel_id=None):
        response = get_hotel(hotel_id)
        return make_response(response.to_json(), 200, headers)

    def post(self):
        args = post_parser.parse_args()
        response = create_hotel(args.name, args.email, args.zip_code, args.phone)
        return make_response(response.to_json(), 200, headers)

    def patch(self, hotel_id=None):
        if hotel_id is not None:
            args = patch_parser.parse_args()
            response = update_hotel(hotel_id, args.name, args.email, args.zip_code, args.phone)
            return make_response(response.to_json(), 200, headers)
        return 400
