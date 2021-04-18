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

    with urllib.request.urlopen(get_news_url, data=None) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results
            
def process_results(news_results):
    
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

def get_articles(source):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.__format__(source,api_key)

    with urllib.request.urlopen(get_articles_url, data=None) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results

def process_articles(articles_results):
    '''
    Function that processes the articles result and transform them to a list of objects
    '''
    #author, title, description, url, date , image, 
    articles_list = []
    for article_item in articles_results:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        date = article_item.get('publishedAt')
        image = article_item.get('urlToImage')

        if date and author and image:
            article_object = Article(author,title,description,url,image,date)
            articles_list.append(article_object)

    return articles_list


        


