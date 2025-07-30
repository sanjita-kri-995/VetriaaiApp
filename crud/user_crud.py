from database.session_manager import get_db_session
from model.models import User
from schema.schemas import SignUpRequest


def create_user(user: SignUpRequest):
    with get_db_session() as db:
        db_user = User(
            username=user.username,
            hashed_password=user.password,
            role=user.role
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

def create_user_from_user(user: User):
    with get_db_session() as db:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

def get_user(username: str):
    with get_db_session() as db:
        return db.query(User).filter(User.username == username).first()

def get_all_user():
    with get_db_session() as db:
        return db.query(User).all()
