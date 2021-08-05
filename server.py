# save this as app.py
from flask import Flask
from flask import render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html', route='https://www.google.com')


@app.route("/route/<string:route>")
def route(route):
	print("route is", route)
	if route == "abc":
		return render_template('index.html', route="https://www.facebook.com")
	return 'hi'