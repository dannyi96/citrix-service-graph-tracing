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

@app.route('/opportunities_page')
def opportunities_page():
	return 'Welcome to our Sales Portal Main Page <br/> These are all our opportunities  <br/> &nbsp;&nbsp; Software Engineer 2  <br/> &nbsp;&nbsp; Principal SW Engineer <br/> &nbsp;&nbsp; PM Engineer'

@app.route('/product_catalogue_page')
def product_catalogue_page():
	response = 'Welcome to the Main Product Catalogue Page. These are a list of all our items'
	response += str(requests.get("http://catalogue-store/catalogue_store_page").content)
	return response

@app.route('/catalogue_store_page')
def catalogue_store_page():
	return 'Items <br/> Item 1 <br/> Item 2 <br/>'

@app.route('/payables_page')
def payables_page():
	return 'Total Payables: $1023'

@app.route('/receivables_page')
def receivables_page():
	return 'Total Receivables: $230'

@app.route('/accounts_page')
def accounts_page():
	response = 'Welcome to the Main Accounts Page. These are a list of all your Receivables & Payables'
	response += str(requests.get("http://payables/payables_page").content)
	response += str(requests.get("http://receivables/receivables_page").content)
	return response

@app.route('/leads')
def leads():
	response = requests.get("http://leads/leads_page")
	return response.content

@app.route('/opportunities')
def opportunities():
	response = requests.get("http://opportunities/opportunities_page")
	return response.content

@app.route('/product_catalogue')
def product_catalogue():
	response = requests.get("http://product-catalogue/product_catalogue_page")
	return response.content

@app.route('/accounts')
def accounts():
	response = requests.get("http://accounts/accounts_page")
	return response.content