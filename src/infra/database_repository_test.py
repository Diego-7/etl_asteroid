import pytest
from .database_connector import DatabaseConnector
from .database_repository import DatabaseRepository

@pytest.mark.skip(reason="No need to insert in database")
def test_insert_asteroid():
    DatabaseConnector.connect()
    
    database_repo = DatabaseRepository()
    
    database_repo.insert_asteroid()