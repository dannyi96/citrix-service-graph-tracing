from flask import Flask, request
import requests
import time

app = Flask(__name__)

TRACE_HEADERS_TO_PROPAGATE = [ \
    'x-ot-span-context',\
    'x-request-id',\
    'X-B3-Traceid',\
    'X-B3-Spanid',\
    'X-B3-ParentSpanid',\
    'X-B3-Sampled',\
    'X-B3-Flags'\
    ]
 
def set_trace_headers(req):
    headers = {}
    for header in TRACE_HEADERS_TO_PROPAGATE:
        if header in req.headers:
            headers[header] = req.headers[header]
    return headers

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
	HEADERS = set_trace_headers(request)
	response = 'Welcome to the Main Product Catalogue Page. These are a list of all our items'
	query_string = ''
	min_range = request.args.get('min_range')
	max_range = request.args.get('max_range')
	query_string += 'min_range=%s'%(min_range) if min_range else ''
	query_string += 'max_range=%s'%(max_range) if max_range else ''
	response += str(requests.get("http://catalogue-store/catalogue_store_page?%s"%(query_string),headers=HEADERS).content)
	return response

@app.route('/catalogue_store_page')
def catalogue_store_page():
	min_range = request.args.get('min_range')
	max_range = request.args.get('max_range')
	response = 'min_range: %s \n max_range:%s'%(min_range,max_range)
	try:
		if min_range and int(min_range) < 0:
			raise
		if max_range and int(max_range) < 0:
			raise
	except:
		return '%s Server Error encountered !!'%(response), 500
	if min_range:
		response += '<br/> Filters Price Above %f'%(float(min_range))
	if max_range:
		response += '<br/> Filters Price Below %f'%(float(max_range))
	response += '<br/> Items <br/> Item 1 <br/> Item 2 <br/>'
	return response

@app.route('/payables_page')
def payables_page():
	return 'Total Payables: $1023'

@app.route('/receivables_page')
def receivables_page():
	return 'Total Receivables: $230'

@app.route('/accounts_page')
def accounts_page():
	HEADERS = set_trace_headers(request)
	response = 'Welcome to the Main Accounts Page. These are a list of all your Receivables & Payables'
	response += str(requests.get("http://payables/payables_page",headers=HEADERS).content)
	response += str(requests.get("http://receivables/receivables_page",headers=HEADERS).content)
	return response

@app.route('/leads')
def leads():
	HEADERS = set_trace_headers(request)
	multimedia = request.args.get('multimedia')
	if multimedia == "yes":
		time.sleep(2)
	response = requests.get("http://leads/leads_page",headers=HEADERS)
	return response.content

@app.route('/opportunities')
def opportunities():
	HEADERS = set_trace_headers(request)
	response = requests.get("http://opportunities/opportunities_page",headers=HEADERS)
	return response.content

@app.route('/product_catalogue')
def product_catalogue():
	HEADERS = set_trace_headers(request)
	query_string = ''
	min_range = request.args.get('min_range')
	max_range = request.args.get('max_range')
	query_string += 'min_range=%s'%(min_range) if min_range else ''
	query_string += 'max_range=%s'%(max_range) if max_range else ''
	response = requests.get("http://product-catalogue/product_catalogue_page?%s"%(query_string),headers=HEADERS)
	return response.content

@app.route('/accounts')
def accounts():
	HEADERS = set_trace_headers(request)
	response = requests.get("http://accounts/accounts_page",headers=HEADERS)
	return response.content
