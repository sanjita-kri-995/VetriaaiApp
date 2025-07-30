import os
from dotenv import load_dotenv

# Load from .env file if present
load_dotenv()
class AppSettings:
    APPLICATION_NAME = os.getenv("APPLICATION_NAME")
    APP_PREFIX = os.getenv("APPLICATION_API_PREFIX")

class DBSettings:
    DATABASE_URL = os.getenv("DATABASE_URL")

class OpenAiSettings:
    OPENAI_TOKEN=os.getenv("OPENAI_KEY")

class JWTSettings:
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


app_settings = AppSettings()
openai_settings = OpenAiSettings()
jwt_settings = JWTSettings()
db_settings = DBSettings()
