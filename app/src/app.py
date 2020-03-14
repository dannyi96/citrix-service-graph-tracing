from flask import Flask, request
import requests
import time
import csv
import random
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

@app.route('/netflix-frontend')
def netflix_frontend():
	return 'Welcome to our Netflix Clone Website!! <br/> We have a lot of features!!!  <br/>'

@app.route('/netflix-tv-shows')
def netflix_tv_shows():
	HEADERS = set_trace_headers(request)
	response = str(requests.get("http://metadata-store-service/netflix-metadata-store?type=movie",headers=HEADERS).content)
	return 'Tv Shows List: %s'%(response)

@app.route('/netflix-movies')
def netflix_movies():
	HEADERS = set_trace_headers(request)
	response = str(requests.get("http://metadata-store-service/netflix-metadata-store?type=tv-show",headers=HEADERS).content)
	return 'Movies List: %s'%(response)

@app.route('/netflix-metadata-store')
def netflix_metdata_store():
	type_param = request.args.get('type',None)
	if type_param == None:
		return 'No Type Parameter Found', 500
	elif type_param=='tv-show':
		return 'Dexter <br/> The Office <br/> Mr Robot <br/>'
	elif type_param=='movie':
		return 'Shutter Island <br/> Shawshank Redemption <br/> Gone Girl <br/>'

@app.route('/telemetry-store')
def telemetry_store():
	type_param = request.args.get('type',None)
	if type_param=='current-trends':
		return 'Shutter Island <br/> Shawshank Redemption <br/> Gone Girl <br/>'
	elif type_param=='similar-shows':
		return 'Mr Robot<br/> Death on the nile <br/> Stranger things<br/>'
	elif type_param == 'mutual-friends-interests':
		return "The girl on the traon <br/> Shawshank Redemption <br/> Gone Girl <br/>'"
	else:
		return 'TYPE NOT FOUND', 500

@app.route('/tv-shows')
def tv_shows():
	HEADERS = set_trace_headers(request)
	response = str(requests.get("http://tv-shows-service/netflix-tv-shows",headers=HEADERS).content)
	return 'TV Show Page: <br/> <br/>' + response

@app.route('/movies')
def movies():
	HEADERS = set_trace_headers(request)
	response = str(requests.get("http://movies-service/netflix-movies",headers=HEADERS).content)
	return 'Movies Page: <br/> <br/>' + response

@app.route('/recommendation-engine')
def recommendation_engine():
	HEADERS = set_trace_headers(request)
	type_param = request.args.get('type',None)
	response = str(requests.get("http://recommendation-engine-service/netflix-recommendation-engine?type=%s"%(type_param),headers=HEADERS).content)
	return response

@app.route('/netflix-recommendation-engine')
def netflix_recommendation_engine():
	HEADERS = set_trace_headers(request)
	type_param = request.args.get('type',None)
	if type_param == 'trending':
		response = requests.get("http://trending-service/netflix-trending?type=current-trends",headers=HEADERS)
	elif type_param == 'similar-shows':
		response = requests.get("http://similarity-calculator-service/netflix-similarity-calculator",headers=HEADERS)
	elif type_param == 'mutual-friends-interests':
		response = requests.get("http://mutual-friends-interests-service/netflix-mutual-friends-interests",headers=HEADERS)
	else:
		response = requests.get("http://trending-service/netflix-trending?type=%s"%(type_param),headers=HEADERS)
	if response.status_code != 200:
		return 'Recommendation Engine Error', 500
	else:
		return str(response.content)

@app.route('/netflix-trending')
def netflix_trending():
	HEADERS = set_trace_headers(request)
	# time.sleep(1)
	type_param = request.args.get('type',None)
	response = requests.get("http://telemetry-store-service/telemetry-store?type=%s"%(type_param),headers=HEADERS)
	if response.status_code != 200:
		return 'Trending Page Error', 500
	return 'Trending Page: <br/> <br/>' + str(response.content)

@app.route('/netflix-similarity-calculator')
def netflix_similarity_calculator():
	HEADERS = set_trace_headers(request)
	# time.sleep(1)
	response = str(requests.get("http://telemetry-store-service/telemetry-store?type=similar",headers=HEADERS).content)
	return 'Similar Shows: <br/> <br/>' + response

@app.route('/netflix-mutual-friends-interests')
def netflix_mutual_friends_interests():
	HEADERS = set_trace_headers(request)
	# time.sleep(1)
	response = str(requests.get("http://telemetry-store-service/telemetry-store?type=mutual-friends-interests",headers=HEADERS).content)
	return 'Mutual Friend interests: <br/> <br/>' + response

