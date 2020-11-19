from flask import Flask, jsonify
from quotes import funny_quotes
from web import website
import random

app = Flask(__name__)

@app.route("/api/funny")
def serve_funny_qoute():
	quotes = funny_quotes()
	nr_of_quotes = len(quotes)
	selected_quote = quotes[random.randint(0, nr_of_quotes - 1)] 
	return jsonify(selected_quote)

@app.route("/")
def homemessage():
	return '<h1 style="text-align:center"> Hellow World </h1>'



if __name__ == "__main__":
	app.run(debug=True)