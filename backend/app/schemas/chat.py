from pydantic import BaseModel, Field
from typing import List, Optional, Literal

Role = Literal["system", "user", "assistant"]

class ChatMessage(BaseModel):
    role: Role
    content: str

class ChatRequest(BaseModel):
    message: str = Field(..., description="User message.")
    model: Optional[str] = Field(None, description="Ollama model name.")
    system: Optional[str] = Field(None, description="System prompt.")
    history: Optional[List[ChatMessage]] = Field(default_factory=list)
    temperature: Optional[float] = None
    num_predict: Optional[int] = None

class ChatResponse(BaseModel):
    model: str
    response: str
    usage: dict
