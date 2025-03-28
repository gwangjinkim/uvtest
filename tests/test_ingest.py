from services.data_ingestion.ingest_data import ingest

def test_ingest_returns_something():
    result = ingest()
    assert result is not None
