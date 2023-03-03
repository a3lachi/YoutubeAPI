from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import json




app = Flask(__name__)
api = Api(app)

class Video(Resource) :
	def get(self):

		s = json.dumps(['chh','345'])
		return s , 200


api.add_resource(Video,'/video')




if __name__ == '__main__':
    app.run()