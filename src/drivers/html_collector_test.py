from .html_collector import HtmlCollector
import urllib.request

def test_request_from_page():
# Define a URL do site com as informações
    url = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY"

# Abre a URL e lê o código HTML
    html = urllib.request.urlopen(url).read()

# Cria uma instância da classe HtmlCollector
    html_collector = HtmlCollector()

# Chama a função collect_essential_information com o código HTML
    essential_information = html_collector.collect_essential_information(html)

# Imprime a informação essencial
    print(essential_information)
    

