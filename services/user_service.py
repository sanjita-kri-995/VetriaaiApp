from crud import user_crud
from model.models import User
from schema.schemas import SignUpRequest


def create_user(user: SignUpRequest):
    return user_crud.create_user(user)

def create_user_from_user(user: User):
    return user_crud.create_user_from_user(user)

def get_user(username: str):
    return user_crud.get_user(username)

def get_all_user():
    return user_crud.get_all_user()

