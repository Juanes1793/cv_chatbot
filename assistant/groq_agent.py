from langchain_groq import ChatGroq
from config.config import ENV_VARIABLES

llm = ChatGroq(
    api_key= ENV_VARIABLES["GROQ_API_KEY"],
    model="llama-3.3-70b-versatile", 
    timeout=None
)

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)