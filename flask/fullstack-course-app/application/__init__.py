from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('home.html')
