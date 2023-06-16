#from flask import Flask
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
@app.route('/')
def index():
    return index('index.html')
@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    if query:

        return redirect('/')
    else:
        return redirect('/')

#url_for('static', filename='style.css')