from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, Flask world</h1>' # return HTML foe the page to display

#app.register_route_route(index, '/')
app.run(debug=True) # start the development server
