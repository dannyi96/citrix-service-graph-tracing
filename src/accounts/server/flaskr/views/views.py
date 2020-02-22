from server.flaskr import app
from flask import render_template
import json


addr = {
	'accounts': '10.106.197.131', # Use env later
	'accounts_port': '7000',
	}

@app.route('/<path>')
def generic_path(path):
    return render_template(path, addr=addr )

@app.route('/')
def index():
    return render_template('index.html', addr=addr)
