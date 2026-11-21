from fastapi import FastAPI
from routers import student

app = FastAPI()

app.include_router(
    student.router,
    prefix="/students",
    tags=["Students"]
)

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}