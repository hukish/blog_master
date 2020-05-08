from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_quotes

@main.route('/')
def index():
    '''
    View root page.
    '''

    

    return render_template('index.html', title=title)
