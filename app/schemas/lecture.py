from datetime import date
from pydantic import BaseModel

class LectureCreate(BaseModel):
    subject: str
    lecture_number: int
    date: date

class LectureOut(BaseModel):
    id: int
    subject: str
    lecture_number: int
    date: date
    teacher_id: int

    class Config:
        from_attributes = True
