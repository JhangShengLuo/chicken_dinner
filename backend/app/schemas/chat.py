from pydantic import BaseModel
from typing import Optional, List

class ChatMessage(BaseModel):
    role: str # "user" or "assistant"
    content: str

class ChatRequest(BaseModel):
    message: str
    provider: str
    language: str = "English" # "English" or "繁體中文"
    history: List[ChatMessage] = []

class ChatResponse(BaseModel):
    reply: str
