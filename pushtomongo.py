from pymongo import MongoClient
from env import MONGO_URI


client = MongoClient(MONGO_URI)

test = client.test

csv = test['csv']

for f in ["partFrame.csv", "eventFrame.csv"]:
    with open(f, 'r') as opened:
        text = opened.read()
        obj = {
            "label": "game1_" + f.split(".")[0],
            "data": text
        }
        csv.insert_one(obj)
