from flask import Flask, render_template, request

from application import app

@app.route("/")
@app.route("/index")
def index():
    return render_template('home.html')
