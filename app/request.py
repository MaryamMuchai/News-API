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

def get_news(category):
    '''
    getting the json response function
    '''
    get_news_url = base_url.format(category,api_key) #passing the api_key and category from the config.py

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results
            
def process_results(news_list):
    
    '''
    processes the news result to list of objects
    '''
     #id, name, description, url, category, language, country
    news_results = []
    for news in news_list:
        id = news.get('id')
        name = news.get('name')
        description = news.get('description')
        url = news.get('url')
        category = news.get('category')
        language = news.get('language')
        country = news.get('country')

        if description:
            news_object = Source(id, name, description, url, category, language, country)
            news_results.append(news_object)
            
    return news_results


        


