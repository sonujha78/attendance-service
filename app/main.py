from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.routers import auth, attendance, lecture

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Attendance Service")

app.include_router(auth.router)
app.include_router(attendance.router)
app.include_router(lecture.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
