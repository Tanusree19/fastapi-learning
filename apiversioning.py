from fastapi import FastAPI

app = FastAPI()

@app.get("/api/v1/employees")
def get_employees_v1():
    return {
        "version": "v1",
        "message": "Employee API version 1"
    }

@app.get("/api/v2/employees/101")
def get_employees_v2():
    return {
        "version": "v2",
        "message": "One Employee"
    }

@app.post("/api/v1/employees")
def create_employee_v1(employee: dict):
    return {
        "version": "v1",
        "message": "Employee created",
        "employee": employee
    }
