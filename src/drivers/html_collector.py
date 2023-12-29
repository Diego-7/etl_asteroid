from typing import List, Dict
from bs4 import BeautifulSoup
from .interfaces.html_collector import HtmlCollectorInterface

class HtmlCollector(HtmlCollectorInterface):
    
    @classmethod
    def collect_essential_information(cls, html: str) -> List[Dict[str, str]]:
        soup = BeautifulSoup(html, 'html.parser')
        
        # Cria uma lista vazia para armazenar as informações essenciais
        essential_info = []
        
        # Busca todos os elementos que contêm as informações dos asteróides
        asteroids = soup.find_all(class_ = 'token-property')
        
        # Percorre os elementos encontrados
        for asteroid in asteroids:
            # Extrai as informações de cada elemento
            asteroid_name = asteroid.find(attrs={'data-label': 'Name'}).text
            absolute_magnitude = asteroid.find(attrs={'data-label': 'Absolute Magnitude'}).text
            is_potentially_hazardous = asteroid.find(attrs={'data-label': 'Potentially Hazardous'}).text
            orbiting_body = asteroid.find(attrs={'data-label': 'Orbiting Body'}).text
            is_sentry_object = asteroid.find(attrs={'data-label': 'Sentry Object'}).text
            
            # Cria um dicionário com as informações do asteróide
            info = {
                'name': asteroid_name,
                'absolute_magnitude': absolute_magnitude,
                'is_potentially_hazardous': is_potentially_hazardous,
                'orbiting_body': orbiting_body,
                'is_sentry_object': is_sentry_object
            }
            
            # Adiciona o dicionário à lista essential_info
            essential_info.append(info)
        
        # Retorna a lista de informações essenciais
        return essential_info
