from abc import ABC, abstractclassmethod
from typing import Dict

class HttpRequesterInterface(ABC):
    
    @abstractclassmethod
    def request_from_page(self) -> Dict[int, str]:
        pass