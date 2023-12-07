from src.errors.load_error import LoadError
from .load_data import LoadData

class RepositorySpy:
    def __init__(self) -> None:
        self.insert_artist_attributes = []
        
    def insert_asteroid(self, data):
        self.insert_asteroid_attributes.append(data)
        
def teste_load():
    repo = RepositorySpy()
    load_data = LoadData(repo)
    
    load_data.load(transform)