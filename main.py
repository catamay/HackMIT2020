from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method=='GET':
        return render_template('site.html')
    else:
        return None
        # handle image upload here

@app.route('/about')
def about_page():
    return"<h1>about page</h1>"