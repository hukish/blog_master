from flask import render_template,request,redirect,url_for,abort
from . import main
from ..requests import get_quotes
from flask_login import login_required
from ..models import User

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''


    title =     title = 'Home - Welcome to The Quote review Website Online'
    return render_template('index.html',title = title)


@main.route('/quote/<int:id>', methods = ['GET','POST'])
@login_required
def quote(quote_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    quote = get_quote(id)
    title = f'{movie.title}'

    return render_template('quote.html',title = title,quote = quote)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
