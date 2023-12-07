from typing import Dict
from abc import ABC, abstractmethod

class DatabaseRepositoryInterface(ABC):
    
    @abstractmethod
    def insert_asteroid(self, data: Dict) -> None:
        pass