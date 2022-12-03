from flask_restful import reqparse, Resource
from flask import make_response, abort  # returns an HTML response
from services.GuestService import *
from flask_jwt_extended import jwt_required, get_jwt_identity

post_parser = reqparse.RequestParser()
post_parser.add_argument('f_name', type=str)
post_parser.add_argument('l_name', type=str)
post_parser.add_argument('email', type=str)
post_parser.add_argument('phone', type=int)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('f_name', type=str)
patch_parser.add_argument('l_name', type=str)
# patch_parser.add_argument('email', type=str)
patch_parser.add_argument('phone', type=int)

headers = {'Content-Type': 'application/json'}


class Guest(Resource):
    @jwt_required()
    def get(self, guest_id=None):
        email_identity = get_jwt_identity()
        if guest_id is None:
            guest = get_guest_by_email(email_identity)
        else:
            guest = get_guest_by_id(guest_id)
        if guest and email_identity == guest.email:
            return make_response(guest.to_json(), 200, headers)
        else:
            return abort(403)

    @jwt_required()
    def post(self):
        email_identity = get_jwt_identity()
        args = post_parser.parse_args()
        if len(args.email) == 0:
            abort(400, "ERROR! email is required.")
        elif email_identity == args.email:
            found_guest = get_guest_by_email(args.email)
            if found_guest is None:
                response = create_guest(args.f_name, args.l_name, args.email, args.phone)
                return make_response(response.to_json(), 200, headers)
            else:
                abort(400, "ERROR! guest with this email already exists.")
        else:
            return abort(403)

    @jwt_required()
    def patch(self, guest_id):
        email_identity = get_jwt_identity()
        guest = get_guest_by_id(guest_id)
        if guest and email_identity == guest.email:
            args = patch_parser.parse_args()
            guest = update_guest(guest_id, args.f_name, args.l_name)
            return make_response(guest.to_json(), 200, headers)
        else:
            abort(403)

    @jwt_required()
    def delete(self, guest_id=None):
        delete_guest(guest_id)
        return make_response("deleted", 200, headers)
    # def get(self, guest_id=None):
    #     response = get_guest(guest_id)
    #     return make_response(response.to_json(), 200, headers)
    #
    # def post(self):
    #     args = post_parser.parse_args()
    #     response = create_guest(args.f_name, args.l_name, args.email, args.phone)
    #     return make_response(response.to_json(), 200, headers)
    #
    # def patch(self, guest_id=None):
    #     if guest_id is not None:
    #         args = patch_parser.parse_args()
    #         response = update_guest(guest_id, args.f_name, args.l_name, args.email, args.phone)
    #         return make_response(response.to_json(), 200, headers)
    #     return 400
    #
    # def delete(self, guest_id=None):
    #     delete_guest(guest_id)
    #     return make_response("deleted", 200, headers)
