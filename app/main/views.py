from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_quotes

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''


    title =     title = 'Home - Welcome to The Quote review Website Online'
    return render_template('index.html',title = title)


@main.route('/quote/<int:id>')
def quote(quote_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    quote = get_quote(id)
    title = f'{movie.title}'

    return render_template('quote.html',title = title,quote = quote)