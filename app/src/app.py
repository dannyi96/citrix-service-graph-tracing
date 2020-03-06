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
	return 'Welcome to our Netflix Clone Website!! Get readt to Netflix & chill'

@app.route('/netflix-frontend')
def netflix_frontend():
	return 'Welcome to our Netflix Clone Website!! <br/> We have a lot of features!!!  <br/> &nbsp;&nbsp; List of shows  <br/> &nbsp;&nbsp; Recommendations  <br/> &nbsp;&nbsp; Friends'

@app.route('/netflix-tv-shows')
def netflix_tv_shows():
	HEADERS = set_trace_headers(request)
	response = requests.get("http://metadata-store/netflix-metadata-store",headers=HEADERS)
	return 'Tv Shows List: %s'%(response.content)

@app.route('/netflix-movies')
def netflix_movies():
	HEADERS = set_trace_headers(request)
	response = requests.get("http://metadata-store/netflix-metadata-store",headers=HEADERS)
	return 'Movies List: %s'%(response.content)

@app.route('/netflix-metadata-store')
def netflix_metdata_store():
	return 'Mr Robot \n Dexter \n Hannibal \n Silicon Valley ....'

@app.route('/tv-shows')
def tv_shows():
	HEADERS = set_trace_headers(request)
	response = requests.get("http://tv-shows/netflix-tv-shows",headers=HEADERS)
	return response.content

@app.route('/movies')
def movies():
	HEADERS = set_trace_headers(request)
	response = requests.get("http://movies/netflix-movies",headers=HEADERS)
	return response.content

@app.route('/recommendation-engine')
def recommendation_engine():
	HEADERS = set_trace_headers(request)
	response = requests.get("http://recommendation-engine/netflix-recommendation-engine",headers=HEADERS)
	return response.content

@app.route('/netflix-recommendation-engine')
def netflix_recommendation_engine():
	HEADERS = set_trace_headers(request)
	response_1 = str(requests.get("http://trending/netflix-trending",headers=HEADERS).content)
	response_2 = str(requests.get("http://similarity-calculator/netflix-similarity-calculator",headers=HEADERS).content)
	response_3 = str(requests.get("http://mutual-friends-interests/netflix-mutual-friends-interests",headers=HEADERS).content)
	return '\n'.join([response_1,response_2,response_3])

@app.route('/netflix-trending')
def netflix_trending():
	return 'Trending: Mr Robot \n Friends \n'

@app.route('/netflix-similarity-calculator')
def netflix_similarity_calculator():
	return 'Similar shows: Dexter \n Big Bang Theory \n'

@app.route('/netflix-mutual-friends-interests')
def netflix_mutual_friends_interests():
	return 'Friends Interests: Silicon Valley \n HTGAWM \n'

