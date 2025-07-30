from fastapi import APIRouter, HTTPException
from auth.auth_utility import hash_password
from model.models import User
from schema.schemas import SignUpRequest
from services import user_service
from services.logger import logger

signup_router = APIRouter()

@signup_router.post("/signup")
async def signup(data: SignUpRequest):
    logger.info("Signup start")
    db_user = user_service.get_user(data.username)
    if db_user:
        logger.warning(f"Signup attempt with existing username: {data.username}")
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_pw = hash_password(data.password)
    new_user = User(username=data.username, hashed_password=hashed_pw, role=data.role)
    new_user = user_service.create_user_from_user(new_user)
    logger.info(f"New user signed up: {new_user.username}")
    return {"message": "User created"}
