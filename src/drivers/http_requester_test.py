from .http_requester import HttpRequester

def test_request_from_page(requests_mock):
    url = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY'
    response_context = '<h1>OlaMundo'
    requests_mock.get(url, status_code=200, text=response_context)
    
    http_requester = HttpRequester()
    request_response = http_requester.request_from_page()
    
    assert 'status_code' in request_response
    assert 'html' in request_response
    assert request_response["status_code"] == 200
    assert request_response["html"] == response_context
    