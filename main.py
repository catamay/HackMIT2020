from flask import Flask
app = Flask(__name__)

@app.route('/')
def home_page():
    return "<h1>homepage</h1>"

@app.route('/about')
def about_page():
    return"<h1>about page</h1>"