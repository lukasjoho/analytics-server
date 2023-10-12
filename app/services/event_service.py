from app.db import db
from app.models.event import EventInsertModel, EventResponseModel
from datetime import datetime

class EventService:
    @staticmethod
    def get_events():
        return db.query('SELECT * FROM events')

    @staticmethod
    def create_event(body: EventInsertModel):
        print("Reached create", body.name)
        timestamp = datetime.strptime(body.timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
        row = [body.name, timestamp, body.type]
        data = [row]
        res = db.insert('events', data, column_names=['name', 'timestamp', 'type'])
        return res