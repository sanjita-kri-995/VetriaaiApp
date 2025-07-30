from typing import Optional, List

from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

class SignUpRequest(BaseModel):
    username : str
    password : str
    role: str

class UserOut(BaseModel):
    id: int
    username: str

class JDRawRequest(BaseModel):
    description: str


class JDRectifySchema(BaseModel):
    id: Optional[int]
    job_title: Optional[str]
    company: Optional[str]
    location: Optional[str]
    salary_range: Optional[str]
    experience_level: Optional[str]
    job_type: Optional[str]
    skills: Optional[List[str]]
    responsibilities: Optional[List[str]]
    requirements: Optional[List[str]]
    benefits: Optional[List[str]]
