from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast




app = Flask(__name__)
api = Api(app)

class Video(Resource) :
	pass 


api.add_ressource(Video,'/video')




if __name__ == '__main__':
    app.run()