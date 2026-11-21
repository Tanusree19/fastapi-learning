from pydantic import BaseModel

# Create a Student model
class Student(BaseModel):
    name: str
    age: int
    course: str

# Create student data
student1 = Student(
    name="Tanu",
    age="hello",
    course="Computer Science"
)

# Display student details
print(student1)
print(student1.name)
print(student1.age)
print(student1.course)