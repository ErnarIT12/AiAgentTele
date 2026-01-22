from pydantic import BaseModel, field_validator, Field
class ChatRequest(BaseModel):
    message: str
    session_id: str | None = None
class AgentResponse(BaseModel):
    answer: str
    session_id: str