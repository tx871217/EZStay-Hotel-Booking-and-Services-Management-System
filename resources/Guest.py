from flask_restful import reqparse, Resource
from flask import make_response  # returns an HTML response
from services.GuestService import *

post_parser = reqparse.RequestParser()
post_parser.add_argument('f_name', type=str)
post_parser.add_argument('l_name', type=str)
post_parser.add_argument('email', type=str)
post_parser.add_argument('phone', type=int)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('f_name', type=str)
patch_parser.add_argument('l_name', type=str)
patch_parser.add_argument('email', type=str)
patch_parser.add_argument('phone', type=int)

headers = {'Content-Type': 'application/json'}


class Guest(Resource):
    def get(self, guest_id=None):
        response = get_guest(guest_id)
        return make_response(response.to_json(), 200, headers)

    def post(self):
        args = post_parser.parse_args()
        response = create_guest(args.f_name, args.l_name, args.email, args.phone)
        return make_response(response.to_json(), 200, headers)

    def patch(self, guest_id=None):
        if guest_id is not None:
            args = patch_parser.parse_args()
            response = update_guest(guest_id, args.f_name, args.l_name, args.email, args.phone)
            return make_response(response.to_json(), 200, headers)
        return 400

    def delete(self, guest_id=None):
        delete_guest(guest_id)
        return make_response("deleted", 200, headers)
