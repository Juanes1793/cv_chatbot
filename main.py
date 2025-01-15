from fastapi import FastAPI
import uvicorn
from assistant.groq_agent import llm
from langchain_core.prompts import ChatPromptTemplate
import asyncio


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

async def generate_chat_responses(message):
    prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that speak in spanish. Your task is to answer questions based on the question of the user",
        ),
        ("human",  "question: {question}"),
    ]
    )

    chain = prompt | llm

    async for chunk in chain.astream(message):
        #content = chunk.replace("\n", "<br>")
        #yield f"data: {chunk.content}\n\n"
        await asyncio.sleep(0.05)
        yield chunk.content

@app.post("/endpoint_test")
async def endpoint_test(input: str):
    prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that speak in spanish. Your task is to answer questions based on the question of the user",
        ),
        ("human",  "question: {question}"),
    ]
)

    chain = prompt | llm
    response = chain.invoke(
        {

            "question": input,
        }
    )

    

    return {"message": response.content}
    

    

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)