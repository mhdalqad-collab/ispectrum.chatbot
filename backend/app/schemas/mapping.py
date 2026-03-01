from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class MappingSuggestRequest(BaseModel):
    columns: List[str] = Field(...)
    target_fields: List[str] = Field(...)
    notes: Optional[str] = None
    model: Optional[str] = None
    temperature: Optional[float] = None
    num_predict: Optional[int] = None

class MappingSuggestResponse(BaseModel):
    model: str
    mapping: Dict[str, str]
    confidence: Dict[str, float]
    explanation: str
