from flask import render_template
from . import main
from ..request import get_news, process_results
from ..models import Source, Article

@main.route('/')
def index():
    '''
    root page function that returns the index page and its data
    '''
    #Getting the popular news list
    science = get_news('science')
    tech = get_news('tech')
    health = get_news('health')
    business = get_news('business')
    sport = get_news('sport')
    entertainment = get_news('entertainment')

    title = 'DailyBoomerang'
    return render_template('index.html',title = title,business = business,sport = sport, entertainment = entertainment, science = science ,health = health, tech = tech)

