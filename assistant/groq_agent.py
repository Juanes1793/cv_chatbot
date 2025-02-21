from langchain_groq import ChatGroq
from config.config import ENV_VARIABLES
from langchain_core.prompts import ChatPromptTemplate


llm = ChatGroq(
    api_key= ENV_VARIABLES["GROQ_API_KEY"],
    model="llama-3.3-70b-versatile", 
    timeout=None
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a helpful assistant that helps to answer questions in spanish.
            """
            ,
        ),
        ("human", "{input}"),
    ]
)

chain = prompt | llm