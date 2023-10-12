import requests
from app.services.event_service import EventService
from app.models.event import EventInsertModel

def test_server():
    assert requests.get("http://127.0.0.1:8000").json() == "Application running"

def test_get_events():
    events = EventService.get_events()
    assert len(events) > 0

def test_create_event():
    new_event = {"name": "Page Viewed", "timestamp": "2021-10-10T15:23:10.123Z", "type": "page"}
    event = EventService.create_event(EventInsertModel(**new_event))
    assert event == None