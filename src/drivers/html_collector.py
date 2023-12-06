from typing import List, Dict
from bs4 import BeautifulSoup

class HtmlCollector():
    
    @classmethod
    def collect_essential_information(cls, html: str) -> List[Dict[str, str]]:
        soup = BeautifulSoup(html, 'html.parser')
        
        # Cria uma lista vazia para armazenar as informações essenciais
        essential_info = []
        
        # Busca todos os elementos que tenham a classe 'token-property'
        asteroid_names = soup.find_all(class_='token-property')
        amhs = soup.find_all(class_='token-property')
        iphas = soup.find_all(class_='token-property')
        orbitingBodies = soup.find_all(class_='token-property')
        isos = soup.find_all(class_='token-property')
        
        # Percorre os elementos encontrados
        for asteroid_name_element, amh_element, ipha_element, orbitingBody_element, iso_element in zip(asteroid_names, amhs, iphas, orbitingBodies, isos):
            # Converte os elementos em strings
            text = str(asteroid_name_element)
            text2 = str(amh_element)
            text3 = str(ipha_element)
            text4 = str(orbitingBody_element)
            text5 = str(iso_element)
            
            # Verifica se as strings contêm as palavras desejadas
            if "name" in text and "absolute_magnitude_h" in text2 and "is_potentially_hazardous_asteroid" in text3 and "orbiting_body" in text4 and "is_sentry_object" in text5:
                # Cria um dicionário com as informações essenciais
                info = {
                    "name": text,
                    "absolute_magnitude_h": text2,
                    "is_potentially_hazardous_asteroid": text3,
                    "orbiting_body": text4,
                    "is_sentry_object": text5
                }
                # Adiciona o dicionário à lista de informações essenciais
                essential_info.append(info)
        
        # Retorna a lista de informações essenciais
        return essential_info
