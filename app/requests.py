import urllib.request,json

import requests

api_key = None
base_url = None
articles_url = None

def configure_request(app):
    global api_key, base_url


def getQuotes():
    response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    if response.status_code == 200:
        print(response.json())
        return response.json()