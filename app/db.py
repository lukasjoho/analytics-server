import os 
from dotenv import load_dotenv
import clickhouse_connect

load_dotenv()

HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')
USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')
INTERFACE = os.environ.get('INTERFACE')

class ClickhouseDB:
    def __init__(self):
        self.client = clickhouse_connect.get_client(interface=INTERFACE, host=HOST, port=PORT, username=USERNAME, password=PASSWORD, verify=True, ca_cert="isrgrootx1.pem")

    def query(self, query):
        query_result = self.client.query(query)
        rows = query_result.result_rows
        columns = query_result.column_names
        json = [dict(zip(columns, row)) for row in rows]
        return json
    
    def insert(self, table, data, column_names=None):
        self.client.insert(table, data, column_names)

def init_db():
    try:
        db = ClickhouseDB()
        print("Connected to database")
        return db    
    except Exception as error:
        print("Error connecting to database")
        print("Error: ", error)

db = init_db()