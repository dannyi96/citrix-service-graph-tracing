from flask import Flask
from flask_restful import Api
from flask_cors import CORS

import server.config as config


app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)
CORS(app)

api = Api(app)


from server.flaskr.views import views
