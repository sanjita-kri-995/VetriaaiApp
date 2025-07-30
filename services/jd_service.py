import os
import re
import shutil

import fitz
from fastapi import File

from crud import jd_crud
from schema.schemas import JDRectifySchema
from services.logger import logger
from utility.jd_parser import extract_jd_data

UPLOAD_DIR = "uploads"

def extract_jd(file: File):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    try:
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        extracted_text = _extract_text_from_pdf(file_location)
        new_raw_jd = jd_crud.create_raw_jd(extracted_text)

        jd_json_str = extract_jd_data(new_raw_jd.description)
        logger.debug(f"Parsed JSON String : {jd_json_str}")
        jd_rectify_obj = jd_crud.create_jd_rectify(jd_json_str)
        return jd_rectify_obj
    except Exception as e:
        logger.error(f"something wrong happen : {e}")
        raise e
    finally:
        _delete_file(file_location)


def update_jd(id:int,jd_data: dict):
    logger.debug(f"Update JD called with id: {id}")
    try:
        return jd_crud.update_jd_rectify(id,jd_data)
    except Exception as e:
        logger.error(f"something wrong happen : {e}")
        raise e



def _extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()
        clean_text = re.sub(r'\s+', ' ', text).strip()
    return clean_text

def _delete_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            logger.debug(f"File '{file_path}' has been deleted successfully.")
        else:
            logger.debug(f"File '{file_path}' does not exist.")
    except Exception as e:
        logger.error(f"An error occurred while deleting the file: {e}")