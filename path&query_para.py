from fastapi import FastAPI


app = FastAPI()
@app.get("/students/{student_id}/details")
def student_details(student_id: int, course: str):
    return {
        "student_id": student_id,
        "course": course
    }