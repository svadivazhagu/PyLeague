from pymongo import MongoClient
import pandas
from env import MONGO_URI

def linearScale(domain, ran):
    def scale(d):
        oldVal = 0
        d = float(d)
        dom = domain[:]
        rran = ran[:]
        if (d <= dom[1] and d >= dom[0]):
            if (dom[0] < dom[1]):
                oldVal = (d - dom[0]) / abs(dom[1] - dom[0])
            else:
                oldVal = (d - dom[1]) / abs(dom[0] - dom[1])
            
            newVal = abs(rran[1] - rran[0]) * oldVal
            if (rran[1] > rran[0]):
                newVal += rran[0]
            else:
                newVal = rran[0] - newVal
            return newVal
        else:
            return None
        
    return scale

client = MongoClient(MONGO_URI)
db = client.test

matches = db['matchSample']

mts = list(matches.find())

with open('output.csv', 'w') as a_file:
    a_file.write(str(mts))

events = [] # full of dicts
participantFrames = []

playerData = []
partIdent = mts[0]['participantIdentities']
parts = mts[0]['participants']

for pi in partIdent:
    obj = pi
    pi['player']['participantId'] = pi['participantId']
    playerData.append(pi['player'])

import collections

def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

for p in parts:
    for key, pd in enumerate(playerData):
        if pd['participantId'] == p['participantId']:
            pd.update(p)
            pd = flatten(pd)
            playerData[key] = pd
            break

print(playerData)

df = pandas.DataFrame(playerData)
df.to_csv("playerData.csv")
# for frame in result[0]['frames']:
#     es = frame['events']
#     for e in es:
#         if 'position' in e:
#             e['x'] = e['position']['x']
#             e['y'] = e['position']['y']
#             del e['position']
#         events.append(e)

#     pfs = frame['participantFrames']
#     for p in pfs:
#         if 'position' in pfs[p]:
#             pfs[p]['x'] = pfs[p]['position']['x']
#             pfs[p]['y'] = pfs[p]['position']['y']
#             del pfs[p]['position']
        
#         pfs[p]['timestamp'] = frame['timestamp']
        
#         participantFrames.append(pfs[p])

# eventFrame = pd.DataFrame(events)
# eventFrame.to_csv("eventFrame.csv")

# # partFrame = pd.DataFrame(participantFrames)
# # # partFrame = partFrame.set_index('timestamp')
# # partFrame.to_csv("partFrame.csv")


# # p1Data = partFrame[partFrame.participantId == 1]
# # p1Data.plot(x='timestamp', y='minionsKilled')



# """
# DataFormat
# Two Sheets
# One for events one for participant frames

# Events:
# timestamp, type, participantId, itemId

# Participant Frames
# timestamp, currentGold, dominionScore, jungleMinionsKilled, level, minionsKilled, participantId, position, teamScore, totalGold, xp
# """
# with open("results.json", 'w') as outputFile:
#     outputFile.write(str(list(matchTimeline.find())))

# # res = pd.DataFrame(list(matches.find()))

# # participants = res['participants']


# # print(res)