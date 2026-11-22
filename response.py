from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Request Model
class Student(BaseModel):
    name: str
    age: int
    course: str
    password: str


# Response Model
class StudentResponse(BaseModel):
    name: str
    age: int
    course: str


@app.post("/students", response_model=StudentResponse)
def create_student(student: Student):

    return {
        "name": student.name,
        "age": student.age,
        "course": student.course,
        "password": student.password
    }