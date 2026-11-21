from fastapi import FastAPI, Depends

app = FastAPI()

# Dependency function
def get_employee():
    return {
    "name": "Arun",
    "department": "AI Engineering"
}

# First endpoint
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}

# Second endpoint
@app.get("/profile")
def get_profile(user: dict = Depends(get_employee)):
    return {
        "message": "User profile",
        "user_details": user
    }   