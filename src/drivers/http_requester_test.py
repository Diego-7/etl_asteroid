from .http_requester import HttpRequester

http_requester = HttpRequester()
request_reponse = http_requester.request_from_page()

print(request_reponse)