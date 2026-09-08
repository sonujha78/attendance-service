from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Lecture(Base):
    __tablename__ = "lectures"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String, nullable=False)
    lecture_number = Column(Integer, nullable=False)  # 1 to 8
    date = Column(Date, nullable=False)
    teacher_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    teacher = relationship("User")
