from models.Users import Users
from utils import get_hash

default_users = {'info@GH.com': 'pw123'}


def create_user(email: str, password_hash: str):
    new_user = Users(email=email, password_hash=password_hash)
    new_user.save()


def find_user_by_email(email: str):
    return Users.objects.filter(email=email).first()


def init_users():  # Initialize the db with default users if there are no existing users
    existing_users = Users.objects()  # List of all rider objects in the db
    if len(existing_users) == 0:
        for user_email in default_users:
            password_hash = get_hash(default_users[user_email].encode('utf-8'))
            create_user(user_email, password_hash)