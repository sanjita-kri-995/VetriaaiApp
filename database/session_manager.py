from contextlib import contextmanager
from database.db import SessionLocal
from services.logger import logger

@contextmanager
def get_db_session():
    db = SessionLocal()
    try:
        logger.debug("DB session started")
        yield db
        logger.debug("DB session completed")
    except Exception as e:
        logger.error(f"DB session error: {e}")
        raise
    finally:
        db.close()
        logger.debug("DB session closed")

