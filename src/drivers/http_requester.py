from typing import Dict
import requests

class HttpRequester:
    
    def __init__(self) -> None:
        self.__url = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY'
        
    def request_from_page(self) -> Dict[int, str]:
        response = requests.get(self.__url)
        return{
            "status_code": response.status_code,
            "html": response.text
        }