from uvtest import main
from uvtest.config import main as config_main
from uvtest.packages.pkg1 import main as pkg1_main
from uvtest.services.data_ingestion import ingest_data

def test_imports():
    assert main.greet() == "Hello from main"
    assert config_main.get_config() == {"key": "value"}
    assert pkg1_main.pkg1_hello() == "Hello from pkg1"
    assert ingest_data.ingest() == "Ingesting data..."
