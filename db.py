import os

from pymongo import MongoClient


DATABASE_HOST = os.environ.get('DATABASE_HOST', 'localhost')
DATABASE_PORT = os.environ.get('DATABASE_PORT', 27017)
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'soma')

mongo_client = MongoClient(DATABASE_HOST, DATABASE_PORT)
db = mongo_client[DATABASE_NAME]
