from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_students():
    return {
        "message": "All students retrieved successfully"
    }

@router.get("/{student_id}")
def get_student(student_id: int):
    return {
        "student_id": student_id,
        "message": "Student details retrieved"
    }