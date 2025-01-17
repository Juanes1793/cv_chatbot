from pydantic import BaseModel, Field
from typing import List, Dict


class ChatInput(BaseModel):
    conversation_id : str = Field(description="The conversation id")
    history : List[Dict[str, str]] = Field(description="The history of the conversation")
