from flask import Flask
from flask.templating import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/contact', method=["POST"])
def contact():

    email, message = request.from["_subject"], request.form["_replyto"]
    
    return print("Contacted")

app.run('0.0.0.0')