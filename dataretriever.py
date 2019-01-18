from pymongo import MongoClient
import pandas as pd
from env import MONGO_URI

client = MongoClient(MONGO_URI)
db = client.test


proplayers = db['proPlayers']

res = pd.DataFrame(list(proplayers.find()))

print(res)