from fastapi import FastAPI
from pydantic import BaseModel
from app.routers import events

app = FastAPI()

app.include_router(events.router)

@app.get("/")
def read_root():
    return "Application running"
