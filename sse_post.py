from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import asyncio

app = FastAPI()


# Request model
class ChatRequest(BaseModel):
    question: str


# Generate response
async def generate_response(question: str):

    words = [
        "Your question is:",
        question,
        "Python is a popular programming language."
    ]

    for word in words:
        yield f"data: {word}\n\n"
        await asyncio.sleep(1)


# POST endpoint
@app.post("/chat")
async def chat(request: ChatRequest):

    return StreamingResponse(
        generate_response(request.question),
        media_type="text/event-stream"
    )