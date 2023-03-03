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
		Yt_df=Yt_df.drop('Commennts',axis=1)
		return jsonify(Yt_df.to_dict(orient='records')) 


api.add_resource(Trending,'/trending')




if __name__ == '__main__':
    app.run()