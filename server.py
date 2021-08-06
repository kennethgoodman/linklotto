# save this as app.py
from flask import Flask,render_template,request
from backend.write import put_route
from backend.read import get_route
from markupsafe import escape
import random
import re

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route('/create_route/', methods = ['POST'])
def create_route():
	def convert_to_url(url):
		# TODO convert to re
		if 'http' in url or 'https' in url:
			return url
		return "http://" + url

	if request.method != 'POST':
		return f"Use a POST, you're doing it wrong, you'll get it next time"
	form_data = request.form
	title = escape(form_data['Name'])
	link_route = ''.join(title.split(" ")) # remove spaces for link
	put_route(
		link_route,
		{
		 convert_to_url(escape(form_data['FirstURL'])): int(form_data['FirstURLPercent']) / 100.0, 
		 convert_to_url(escape(form_data['SecondURL'])): int(form_data['SecondURLPercent']) / 100.0
		},
		title
	)
	return f"date saved, link is http://3.16.206.192:5000/route/{escape(form_data['Name'])}"


@app.route("/route/<string:link_route>")
def route(link_route):
	routes = get_route(link_route)
	routes = routes['Item']
	url = random.choices(routes['urls'], weights=list(map(lambda x: float(x), routes['weights'])), k=1)[0]
	return render_template('routing.html', route=url, title=routes.get('title', link_route))
