from datetime import date
from pydantic import BaseModel
from app.models.attendance import StatusEnum

class MarkAttendanceRequest(BaseModel):
    student_id: int
    lecture_id: int
    status: StatusEnum

class AttendanceOut(BaseModel):
    id: int
    student_id: int
    lecture_id: int
    status: StatusEnum

    class Config:
        from_attributes = True

class LectureAttendanceOut(BaseModel):
    lecture_id: int
    subject: str
    lecture_number: int
    date: date
    status: StatusEnum

    class Config:
        from_attributes = True
