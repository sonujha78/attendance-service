from sqlalchemy import Column, Integer, ForeignKey, Enum, UniqueConstraint
import enum
from sqlalchemy.orm import relationship
from app.database import Base

class StatusEnum(str, enum.Enum):
    present = "present"
    absent = "absent"

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    lecture_id = Column(Integer, ForeignKey("lectures.id"), nullable=False)
    status = Column(Enum(StatusEnum), nullable=False)

    student = relationship("User")
    lecture = relationship("Lecture")

    __table_args__ = (
        UniqueConstraint("student_id", "lecture_id", name="unique_student_lecture"),
    )
