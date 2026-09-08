from fastapi import FastAPI

app = FastAPI(title="Student Attendance Service")

@app.get("/health")
def health_check():
    return {"status": "ok"}
