#league app 1/18/19
from riotwatcher import RiotWatcher, ApiError
import pymongo



#Establishing default values if need to be used for testing features.
SUMMONER_NAMES = ['TF Blade', 'SHERNFIRE', 'Santorin', 'Humble Diligent', 'EricZYang', 'Vu1c4n', 'ULookSoCharming', 'deftIy',
                  'Johnsun', 'Pobelter', 'Nugeek', 'ashketchups', 'Winter', 'NintendudeX', 'Soulmario', 'Competition9', 'duoking1',
                  'Dragoonsmash', 'Jurassiq', '2p0', 'Niles', 'Repfix', '5fire', 'insanityxxx', 'Tactical']


SUMMONER_REGION = 'na1'

#load api key in
with open('key.txt', 'r') as key:
    API_KEY = key.read().replace('\n', '')

#load atlas key in
with open('atlas.txt', 'r') as key:
    ATLAS_URI = key.read().replace('\n', '')

watcher = RiotWatcher(API_KEY, v4=True)
client = pymongo.MongoClient(ATLAS_URI)

db = client.test

db_list = client.list_database_names()
if "db" in db_list:
    print("db exists")
col = db["champs"]

#Code to collect and push 25 challenger players to Mongo ALREADY DONE
# for i in SUMMONER_NAMES:
#     summoner = watcher.summoner.by_name(SUMMONER_REGION, i)
#     db["proPlayers"].insert_one(summoner)

#x = col.insert(summoner_by_name)

#request for summonerByName() on Doublelift
#test_summoner = watcher.summoner.by_name(SUMMONER_REGION, SUMMONER_NAME)
#print(test_summoner)

version = (watcher.data_dragon.versions_for_region(SUMMONER_REGION))['v']

static_champ_list = watcher.data_dragon.champions(version, True)

data = static_champ_list['data']

champList = []

for key in data.keys():
   champList.append(data[key])

x = col.insert_many(champList)




