from sqlalchemy import Column, String, Integer, ARRAY, Text, Boolean

from database.db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String)

class JDRaw(Base):
    __tablename__ = "jd_raw"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)


class JDRectify(Base):
    __tablename__ = 'jd_rectify'

    id = Column(Integer, primary_key=True)
    job_title = Column(String, nullable=True)
    company = Column(String, nullable=True)
    location = Column(String, nullable=True)
    salary_range = Column(String, nullable=True)
    experience_level = Column(String, nullable=True)
    job_type = Column(String, nullable=True)
    skills = Column(ARRAY(String), nullable=True)
    responsibilities = Column(ARRAY(String), nullable=True)
    requirements = Column(ARRAY(String), nullable=True)
    benefits = Column(ARRAY(String), nullable=True)

