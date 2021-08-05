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
		non_http_portion = "[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
		http_www_portion = "http(s)?:\/\/(www\.)?"
		# if has http or https TODO: combine these
		if re.search(http_www_portion + non_http_portion, url):
			return url
		return "http://" + url


	if request.method == 'GET':
		return f"The URL /data is accessed directly. Try going to '/form' to submit form"
	if request.method == 'POST':
		form_data = request.form
		print(put_route(
			escape(form_data['Name']),
			{convert_to_url(escape(form_data['FirstURL'])): .5, convert_to_url(escape(form_data['SecondURL'])): .5}
		))
		print(form_data)
		return f"date saved, link is http://3.16.206.192:5000/route/{escape(form_data['Name'])}"


@app.route("/route/<string:link_route>")
def route(link_route):
	print("link route is", link_route)
	routes = get_route(link_route)
	print(routes)
	routes = routes['Item']
	url = random.choices(routes['urls'], weights=list(map(lambda x: float(x), routes['weights'])), k=1)[0]
	return render_template('routing.html', route=url)
