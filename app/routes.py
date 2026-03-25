from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Gayathri'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Madurai!'
        },
        {
            'author': {'username': 'Priya'},
            'body': 'Learning Flask is fun!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)