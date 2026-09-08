from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.models.lecture import Lecture
from app.models.attendance import Attendance
from app.schemas.attendance import MarkAttendanceRequest, AttendanceOut, LectureAttendanceOut
from app.core.dependencies import require_teacher, require_student

router = APIRouter(prefix="/attendance", tags=["Attendance"])


@router.post("/mark", response_model=AttendanceOut)
def mark_attendance(
    payload: MarkAttendanceRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_teacher),
):
    lecture = db.query(Lecture).filter(Lecture.id == payload.lecture_id).first()
    if not lecture:
        raise HTTPException(status_code=404, detail="Lecture not found")

    if lecture.teacher_id != current_user.id:
        raise HTTPException(status_code=403, detail="You do not teach this lecture")

    student = db.query(User).filter(User.id == payload.student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    record = db.query(Attendance).filter(
        Attendance.student_id == payload.student_id,
        Attendance.lecture_id == payload.lecture_id,
    ).first()

    if record:
        record.status = payload.status
    else:
        record = Attendance(
            student_id=payload.student_id,
            lecture_id=payload.lecture_id,
            status=payload.status,
        )
        db.add(record)

    db.commit()
    db.refresh(record)
    return record


@router.get("/me", response_model=list[LectureAttendanceOut])
def view_my_attendance(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_student),
):
    records = (
        db.query(Attendance)
        .filter(Attendance.student_id == current_user.id)
        .join(Lecture, Attendance.lecture_id == Lecture.id)
        .all()
    )

    return [
        LectureAttendanceOut(
            lecture_id=r.lecture.id,
            subject=r.lecture.subject,
            lecture_number=r.lecture.lecture_number,
            date=r.lecture.date,
            status=r.status,
        )
        for r in records
    ]
