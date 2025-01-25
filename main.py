import uvicorn
import json
import asyncio
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from assistant.schemas import ChatInput
from assistant.groq_agent import chain



app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


async def generate_chat_responses(message):
    async for chunk in chain.astream(message):
        #content = chunk.replace("\n", "<br>")
        #yield f"data: {chunk.content}\n\n"
        await asyncio.sleep(0.05)
        yield chunk.content

async def generate_chat_responses_event(message):
    async for event in chain.astream_events(message, version="v2"):
        if event["event"] == "on_chat_model_stream":
            await asyncio.sleep(0.05)
            # Envía el chunk en formato JSON
            chunk_data = json.dumps({"content": event["data"]["chunk"].content})
            yield f"{chunk_data}\n"
        elif event["event"] == "on_chat_model_end":
            yield '{"content": "on_chat_model_end"}\n'


@app.post("/chat_stream", tags=["Streaming"])
async def chat_stream(input: ChatInput) -> StreamingResponse:
    #converstation_id = input.conversation_id
    history = input.history
    question = history[-1]["content"]
    return StreamingResponse(
        generate_chat_responses(message=question),
        media_type="application/json"  # Especifica que el contenido es JSON
    )


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)