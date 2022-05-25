from flask import Flask # we may need ot pip install flask
from flask import render_template # this bit lets us show html web pages
import json



# Flask is a proper web server. Handles basic html with parameters
app = Flask(__name__)
# declare routes for our app
@app.route('/') # this is the ROOT of our service
def root():
    return 'Hello' # we return any simple or complex html

@app.route('/home')
def home():
    content = '<h2>Time for Coffee</h2>'
    return content


if __name__ == '__main__':
    # to exercise this code
    # - run this module which will create a Flash server instance
    # - open a browser at http://127.0.0.1:5000 (default Flask values)
    # NB we must cycle the server to see any changes
    app.run() # call our app into play