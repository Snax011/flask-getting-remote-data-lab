import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Sends a GET request and returns the raw response body (bytes)
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        # Parses the raw response body into Python data structures
        return json.loads(self.get_response_body())