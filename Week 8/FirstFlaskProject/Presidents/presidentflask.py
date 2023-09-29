from flask import Flask, render_template

from president import President

app = Flask(__name__)

@app.route('/')
def index():
    """Default page for this site"""
    return '''<h1>try .../president/#<h1>'''

@app.route('/president/<termnum>')
def president_by_term(termnum):
    """Retrieve president information for specifid term number"""
    term = int(termnum)
    if 0 < term < 45:
        president = President(term)
        html_content = f'<h2>Last name for President #{term}: {president.last_name}, First Name: {president.first_name}<h2>'
        return html_content
    else:
        html_content = '<h2>Sorry, {} is not a valid term number<h2>'.format(term)
        return html_content
    
    if presidents:
        return render_template('president_results.html,').format(term)
        
    
    