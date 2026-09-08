from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.models.lecture import Lecture
from app.schemas.lecture import LectureCreate, LectureOut
from app.core.dependencies import require_teacher

router = APIRouter(prefix="/lectures", tags=["Lectures"])


@router.post("/", response_model=LectureOut)
def create_lecture(
    payload: LectureCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_teacher),
):
    lecture = Lecture(
        subject=payload.subject,
        lecture_number=payload.lecture_number,
        date=payload.date,
        teacher_id=current_user.id,
    )
    db.add(lecture)
    db.commit()
    db.refresh(lecture)
    return lecture
