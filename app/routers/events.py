from app.models.event import EventInsertModel
from fastapi import APIRouter
from app.services.event_service import EventService

router = APIRouter(
    prefix="/events",
    tags=["events"]
)

@router.get("/")
async def read_track_events():
    return EventService.get_events()

@router.post("/")
async def create_event(body: EventInsertModel):
    return EventService.create_event(body)