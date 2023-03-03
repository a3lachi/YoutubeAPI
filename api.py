from flask import Flask , jsonify
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import json
from YTScrap import *



app = Flask(__name__)
api = Api(app)

class Trending(Resource) :
	def get(self):
		Yt_df = GetTrendingVideos()
		Yt_df=Yt_df.drop('Comments', axis=1)
		return jsonify(Yt_df.to_dict(orient='records')) 

class Video(Resource) :
	def post(self):
	    parser = reqparse.RequestParser()  # initialize
	    
	    parser.add_argument('url', required=True)  # add args
	    parser.add_argument('name', required=True)
	    parser.add_argument('city', required=True)
	    
	    args = parser.parse_args()  # parse arguments to dictionary
	    
	    # create new dataframe containing new values
	    new_data = pd.DataFrame({
	        'userId': args['userId'],
	        'name': args['name'],
	        'city': args['city'],
	        'locations': [[]]
	    })

api.add_resource(Trending,'/trending')
api.add_resource(Video,'/video')




if __name__ == '__main__':
    app.run()