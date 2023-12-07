from typing import Dict
from .database_connector import DatabaseConnector
from .interfaces.database_repository import DatabaseRepositoryInterface

class DatabaseRepository(DatabaseRepositoryInterface):
    
    @classmethod
    def insert_asteroid(cls, data: Dict) -> None:
        query = '''
            INSERT INTO asteroids
            (asteroid_name, absolute_magnitude_h, is_potentially_hazardous, orbiting_body, is_sentry_object, extraction_date)
            VALUES
            (%s, %s, %s, %s, %s, %s)
        '''
        
        cursor = DatabaseConnector.connection.cursor()
        cursor.execute(query, list(data.values()))
        
        DatabaseConnector.connection.commit()