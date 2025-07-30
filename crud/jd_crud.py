from database.session_manager import get_db_session
from model.models import JDRaw, JDRectify
from schema.schemas import JDRectifySchema


def create_raw_jd(extracted_text: str):
    with get_db_session() as db:
        new_raw_jd = JDRaw(description=extracted_text)
        db.add(new_raw_jd)
        db.commit()
        db.refresh(new_raw_jd)
        return new_raw_jd

def create_jd_rectify(jd_json: dict):
    with get_db_session() as db:
        jd_rectify_obj = JDRectify(**jd_json)
        db.add(jd_rectify_obj)
        db.commit()
        db.refresh(jd_rectify_obj)
        return jd_rectify_obj

def update_jd_rectify(id:int,update_jd_data: dict):
    with get_db_session() as db:
        db_jd = db.query(JDRectify).filter(JDRectify.id == id).first()
        #update_data = update_jd_data.model_dump(exclude_unset=True)

        for key, value in update_jd_data.items():
            setattr(db_jd, key, value)
        db.commit()
        db.refresh(db_jd)
        return db_jd


