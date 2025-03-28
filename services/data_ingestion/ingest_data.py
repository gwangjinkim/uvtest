from config.connection_config import get_connection_info
from pkg1.utils import fetch_data
from pkg2.core import process_data

def ingest():
    conn = get_connection_info()
    raw_data = fetch_data(conn)
    return process_data(raw_data)

def main():
    result = ingest()
    print(f"Data ingestion result: {result}")
