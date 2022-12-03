from datetime import timedelta

from flask import jsonify, make_response
from flask_restful import reqparse, Resource
from flask import abort

from services.UserService import *
from flask_jwt_extended import create_access_token
from utils import get_hash

login_parser = reqparse.RequestParser()
login_parser.add_argument('email', type=str, default="")
login_parser.add_argument('password', type=str, default="")


class Session(Resource):

    def post(self):
        args = login_parser.parse_args()
        if len(args.email) == 0 or len(args.password) == 0:
            abort(400, 'email and password are required fields')
        found_user = find_user_by_email(args.email)
        if found_user:
            password_hash = get_hash(args.password.encode('utf-8'))
            if password_hash == found_user.password_hash:
                access_token = create_access_token(identity=args.email, expires_delta=timedelta(seconds=900))
                return make_response(jsonify(access_token=access_token), 200)
        abort(401, "Invalid credentials")
