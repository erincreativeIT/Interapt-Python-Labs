from flask import Flask, url_for
from knight import Knight

app = Flask(__name__)

@app.route('/')
def index():
    page = '<h1>Knights of the Round Table</h1>\n'
    for knight in Knight.get_knight_names():
        link = '<a href= "{0}">{1}</a>br/>\n'.format(
            url_for('knights', name=knight),
            knight
        )
        page += link
    return page

@app.route('/knights/<name>')
def knights(name):
    knight = Knight(name)
    return '''
    <h1>{0} {1}</h1>
    Favorite color: {2}

    '''