from dotenv import load_dotenv
import os
import pymongo
# import fetch # fetching data is written in a separate script
from flask import Flask, jsonify

load_dotenv() # use dotenv to hide sensitive credential as environment variables
DATABASE_URL=f'mongodb://jt27664Mongo:<password>@flaskmongoherokucluster.rtngq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority' # get connection url from environment

client=pymongo.MongoClient(DATABASE_URL) # establish connection with database
mongo_db=client.db

app=Flask(__name__)

@app.route('/')
def index(): 
  	return 'Use /all_launches_timeline'

@app.route('/sample_launch/')
def sample():
	results=mongo_db.launches.find_one({}, {'_id': 0})
	return jsonify(results)

if __name__ == '__main__':
	app.run()