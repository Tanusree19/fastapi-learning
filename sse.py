from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()


async def generate_events():
    messages = [
        "Hello!",
        "Welcome to FastAPI.",
        "This is SSE streaming.",
        "Data is arriving continuously."
    ]

    for message in messages:
        yield f"data: {message}\n\n"
        await asyncio.sleep(1)


@app.get("/stream")
async def stream_data():
    return StreamingResponse(
        generate_events(),
        media_type="text/event-stream"
    )

@app.get("/countdown")
async def countdown():
    async def event_generator():
        for i in range(10, 0, -1):
            yield f"data: {i}\n\n"
            await asyncio.sleep(1)
        yield "data: Countdown finished!\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )


from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str


@app.post("/chat/stream")
async def chat_stream(request: ChatRequest):

    async def event_generator():
        words = [
            "You",
            "asked:",
            request.message,
            "This",
            "is",
            "a",
            "streaming",
            "response."
        ]

        for word in words:
            yield f"data: {word}\n\n"
            await asyncio.sleep(0.5)

        yield "data: [DONE]\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )
