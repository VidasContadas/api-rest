# coding=utf-8
from flask import Flask
from pymongo import MongoClient

from bson.json_util import dumps

from settings import DATABASE, DEBUG

app = Flask(__name__)
CL = MongoClient()


@app.route("/api/v1/<collection>", methods=['GET'])
def collection_data(collection):
    db = CL[DATABASE]
    try:
        collection = db[collection]
    except Exception as e:
        print(e)
        raise
    cursor = collection.find()
    json_data = dumps([item for item in cursor])
    return json_data

if __name__ == "__main__":
    app.debug = DEBUG
    app.run()
