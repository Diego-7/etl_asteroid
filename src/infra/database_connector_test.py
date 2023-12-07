from .database_connector import DatabaseConnector

def test_connect():
    assert DatabaseConnector.connection == None
    DatabaseConnector.connect()
    assert DatabaseConnector.connection is not None