from flask import Flask
import requests

app = Flask(__name__)
@app.route('/')
def main_page():
	return 'Welcome to our Sales Portal Main Page'

@app.route('/sales_portal')
def sales_portal():
	return 'Welcome to our Sales Portal Main Page <br/> We have a lot of features!!!  <br/> &nbsp;&nbsp; Leads  <br/> &nbsp;&nbsp; Accounts  <br/> &nbsp;&nbsp; Product Catalogue'

@app.route('/leads_page')
def leads_page():
	return 'Welcome to our Sales Portal Main Page <br/> These are all our leads  <br/> &nbsp;&nbsp; Leads  <br/> &nbsp;&nbsp; Mr. X  <br/> &nbsp;&nbsp; Mr. Y'

@app.route('/leads')
def leads():
	try:
		r = requests.get("http://leads/leads_page")
		return r.content
	except:
		return 'Unable to connect to Leads service'

