from flask import render_template
from . import main
from ..request import get_news, process_results
from ..models import Source, Article

@
