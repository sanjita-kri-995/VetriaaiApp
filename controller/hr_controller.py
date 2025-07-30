from fastapi import APIRouter
from pydantic.v1 import BaseModel
from schema import schemas
from services import user_service
from services.logger import logger
from utility.obj_serializer import list_to_json

hr_router = APIRouter()
# hr_router = APIRouter(
#     tags=["hr"],
#     dependencies=[Depends(authenticate_user)]
# )

class HRRequest(BaseModel):
    username: str

@hr_router.get("/hrlist", response_model=list[schemas.UserOut])
async  def hr_list():
    all_users = user_service.get_all_user()
    logger.info("All hr list : %s", list_to_json(all_users))
    return all_users


