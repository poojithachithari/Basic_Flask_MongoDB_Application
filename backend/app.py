from flask import Flask, jsonify, request
from dotenv import load_dotenv
import pymongo
import os
load_dotenv()

MONGO_URL = os.getenv('MONGO_URL')
client = pymongo.MongoClient(MONGO_URL)
db = client.test 

collection = db['signup-form']
app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)