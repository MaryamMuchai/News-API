import urllib.request, json
from .models import Source, Article

#Getting the Api Key
api_key = None
# Base URL
base_url = None

def config_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

