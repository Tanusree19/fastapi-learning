from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Student model
class Student(BaseModel):
    name: str
    age: int
    course: str

# Temporary storage
students = []

# Home endpoint
@app.get("/")
def home():
    return {"message": "Student Management API"}

# POST - Create student
@app.post("/students")
def create_student(student: Student):
    students.append(student)
    return {
        "message": "Student created successfully",
        "student": student
    }

# GET - Retrieve all students
@app.get("/students")
def get_students():
    return students

# PUT - Update student
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):

    if student_id < 0 or student_id >= len(students):
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    students[student_id] = updated_student

    return {
        "message": "Student updated successfully",
        "student": updated_student
    }

# DELETE - Remove student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    if student_id < 0 or student_id >= len(students):
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    deleted_student = students.pop(student_id)

    return {
        "message": "Student deleted successfully",
        "student": deleted_student
    }

