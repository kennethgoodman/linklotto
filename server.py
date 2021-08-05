# save this as app.py
from flask import Flask,render_template,request
from backend.write import put_route
from backend.read import get_route
from markupsafe import escape
import random

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route('/create_route/', methods = ['POST'])
def create_route():
	if request.method == 'GET':
		return f"The URL /data is accessed directly. Try going to '/form' to submit form"
	if request.method == 'POST':
		form_data = request.form
		print(put_route(
			escape(form_data['Name']),
			{escape(form_data['FirstURL']): .99, escape(form_data['SecondURL']): .01}
		))
		print(form_data)
		return f"date saved"


@app.route("/route/<string:link_route>")
def route(link_route):
	routes = get_route(link_route)['Item']
	url = random.choices(routes['urls'], weights=list(map(lambda x: float(x), routes['weights'])), k=1)[0]
	return render_template('routing.html', route=url)
