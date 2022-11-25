from flask_restful import reqparse, Resource
from flask import make_response, abort  # returns an HTML response
from services.HotelService import *

# from flask_jwt_extended import jwt_required, get_jwt_identity

post_parser = reqparse.RequestParser()
# post_parser.add_argument('id', type=str)
post_parser.add_argument('name', type=str)
post_parser.add_argument('email', type=str)
post_parser.add_argument('zip_code', type=int)
post_parser.add_argument('phone', type=int)
# post_parser.add_argument('pw', type=str)

patch_parser = reqparse.RequestParser()
# patch_parser.add_argument('name', type=str)
# patch_parser.add_argument('email', type=str)
patch_parser.add_argument('zip_code', type=int)
patch_parser.add_argument('phone', type=int)

headers = {'Content-Type': 'application/json'}


class Hotel(Resource):
    # @jwt_required()
    def get(self, hotel_id=None):
        # email_identity = get_jwt_identity()
        # if hotel_id is None:
        #     hotel = get_hotel_by_email(email_identity)
        # else:
        #     hotel = get_hotel_by_id(hotel_id)
        # if hotel and email_identity == hotel.email:
        #     return make_response(hotel.to_json(), 200, headers)
        # else:
        #     return abort(403)
        response = get_hotel(hotel_id)
        return make_response(response.to_json(), 200, headers)

    # @jwt_required()
    def post(self):
        # email_identity = get_jwt_identity()
        # args = post_parser.parse_args()
        # if len(args.name) == 0 or len(args.email) == 0:
        #     abort(400, "ERROR! name and email are required fields.")
        # elif email_identity == args.email:
        #     found_hotel = get_hotel_by_email(args.email)
        #     if found_hotel is None:
        #         response = create_hotel(args.name, args.email, args.zipcode, args.phone)
        #         return make_response(response.to_json(), 200, headers)
        #     else:
        #         abort(400, "ERROR! hotel with this email already exists.")
        # else:
        #     return abort(403)

        args = post_parser.parse_args()
        response = create_hotel(args.name, args.email, args.zip_code, args.phone)
        return make_response(response.to_json(), 200, headers)

    # @jwt_required()
    def patch(self, hotel_id):
        # email_identity = get_jwt_identity()
        # hotel = get_hotel_by_id(hotel_id)
        # if hotel and email_identity == hotel.email:
        #     args = patch_parser.parse_args()
        #     hotel = update_hotel(hotel_id, args.email, args.zipcode, args.phone)
        #     return make_response(hotel.to_json(), 200, headers)
        # else:
        #     abort(403)
        if hotel_id is not None:
            args = patch_parser.parse_args()
            response = update_hotel(hotel_id, args.name, args.email, args.zip_code, args.phone)
            return make_response(response.to_json(), 200, headers)
        return 400

    # @jwt_required()
    def delete(self, hotel_id):
        # email_identity = get_jwt_identity()
        # hotel = get_hotel_by_id(hotel_id)
        # if hotel and email_identity == hotel.email:
        #     delete_hotel(hotel_id)
        #     return make_response("deleted", 200, headers)
        # else:
        #     abort(403)
        delete_hotel(hotel_id)
