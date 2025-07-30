from fastapi import APIRouter, HTTPException, Depends, Response, Request
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from fastapi.responses import JSONResponse

from config import jwt_settings
from auth.auth_utility import verify_password
from schema.schemas import LoginRequest
from services import user_service
from services.logger import logger
from auth.jwt_token import create_access_token
from datetime import timedelta

auth_router = APIRouter()

@auth_router.post("/login")
async def login(data: LoginRequest, res: Response):
    db_user = user_service.get_user(data.username)
    if not db_user or not verify_password(data.password, db_user.hashed_password):
        logger.error(f"Invalid login for {data.username}")
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(
        data={"username": data.username, "role": db_user.role},
        expires_delta=timedelta(minutes=30)
    )

    res.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=3600
    )
    logger.info(f"JWT token issued for {data.username}")
    return JSONResponse(content={"username": db_user.username, "role": db_user.role}, status_code=200)

# Secret key and algorithm used to encode/decode JWT
SECRET_KEY = jwt_settings.SECRET_KEY
ALGORITHM = jwt_settings.ALGORITHM
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="hrapp/login")

# Function to get current user from token
def get_current_user(request: Request):
    token = request.cookies.get("access_token")
    try:
        logger.info("Token ===== %s", token)
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("username")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"username": username, "role": payload.get("role")}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Protected route to get user info
@auth_router.get("/user")
def read_user_info(current_user: dict = Depends(get_current_user)):
    return current_user