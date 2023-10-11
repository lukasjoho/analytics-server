from fastapi import FastAPI
import clickhouse_connect
import os 
from dotenv import load_dotenv

load_dotenv()

HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')
USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')
INTERFACE = os.environ.get('INTERFACE')

client = clickhouse_connect.get_client(interface=INTERFACE, host=HOST, port=PORT, username=USERNAME, password=PASSWORD, verify=True, ca_cert="isrgrootx1.pem")

app = FastAPI()


@app.get("/")
def read_root():
    return "Application running"

@app.get("/track")
def read_track():
    query_result = client.query('SELECT * FROM events')
    rows = query_result.result_rows
    columns = query_result.column_names
    json = [dict(zip(columns, row)) for row in rows]
    return json

@app.post("/track")
def track_event():
    return "Event tracked"

@app.post("/page")
def page_event():
    return "Page tracked"

