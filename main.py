from fastapi import FastAPI, APIRouter
from config import app_settings
from starlette.middleware.cors import CORSMiddleware

from controller.jd_controller import jd_router
from controller.hr_controller import hr_router
from controller.signup import signup_router

from auth.login import auth_router
from database.db import engine
from model import models


# Create tables
models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:3000",
    "https://yourdomain.com",
]

hrapp = FastAPI(title=app_settings.APPLICATION_NAME)
hrapp.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

def add_route(route: APIRouter):
    hrapp.include_router(route, prefix=app_settings.APP_PREFIX)

add_route(auth_router)
add_route(signup_router)
add_route(hr_router)
add_route(jd_router)
