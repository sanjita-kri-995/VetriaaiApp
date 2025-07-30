from fastapi import APIRouter, File, UploadFile, HTTPException

from schema.schemas import JDRectifySchema
from services import jd_service
from services.logger import logger

jd_router = APIRouter(
    tags=["JD upload"]
)

@jd_router.post("/upload/", response_model=JDRectifySchema)
async def upload_file(file: UploadFile = File(...)):
    try:
        return jd_service.extract_jd(file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@jd_router.put("/update-jd/{jd_id}")
def update_jd(jd_id: int, jd_data:dict):
    logger.debug(f"enter into jd_service : {jd_id} and {jd_data}")
    db_jd = jd_service.update_jd(jd_id,jd_data)

    if not db_jd:
        logger.debug(f"enter into jd_service, {db_jd}")
        raise HTTPException(status_code=404, detail="JD not found")
    return db_jd


