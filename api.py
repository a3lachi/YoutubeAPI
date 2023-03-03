from flask import Flask , jsonify , request
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


api.add_resource(Trending,'/trending')



# class Video(Resource) :

# 	def post(self):
# 	    parser = reqparse.RequestParser()  
# 	    parser.add_argument('url', required=True)
# 	    parser.add_argument('nmbcom', required=False)

	    
# 	    args = parser.parse_args()  
# 	    nmbcomz = 20
# 	    if args.nmbcom :
# 	    	nmbcomz = args['nmbcom']

# 	    url = 'https://www.youtube.com/watch?v='+args.url

# 	    
	    
# 	    # create new dataframe containing new values
# 	    df = pd.DataFrame({
# 	        'Url': args['url'],
# 	        'Video': '',
# 	        'Comments': comz
# 	    })

# 	    return jsonify(df.to_dict(orient='records')) 

class Video(Resource) :

	def post(self):

		url = request.args.get('url')

		url = 'https://www.youtube.com/watch?v=' + url

		nmbComz = request.args.get('nmbcoms')

		if not nmbcomz :
			nmbComz = 10
		comz = ScrapUrl(url,nmbcomz//5)
		comz  = '\n'.join(comz)

		df = pd.DataFrame({'Url': url, 'Comments': comz })

		

		return jsonify(df.to_dict(orient='records')) 




api.add_resource(Video,'/video')




if __name__ == '__main__':
    app.run()