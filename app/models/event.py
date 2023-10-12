from pydantic import BaseModel

class EventInsertModel(BaseModel):
    name: str
    timestamp: str
    type: str

class EventResponseModel(EventInsertModel):
    id: str
    received_at: str
