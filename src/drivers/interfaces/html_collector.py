from abc import ABC, abstractclassmethod
from typing import List, Dict

class HtmlCollectorInterface(ABC):
    
    @abstractclassmethod
    def collect_essential_information(self, html: str) -> List[Dict[str, str]]:
        pass