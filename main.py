from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "Analytics API running"

@app.post("/track")
def track_event():
    return "Event tracked"

@app.post("/page")
def page_event():
    return "Page tracked"
