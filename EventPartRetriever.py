from pymongo import MongoClient
import pandas as pd
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

matchTimeline = db['matchTimeline']
result = list(matchTimeline.find())

events = [] # full of dicts
participantFrames = []

for frame in result[0]['frames']:
    es = frame['events']
    for e in es:
        if 'position' in e:
            e['x'] = e['position']['x']
            e['y'] = e['position']['y']
            del e['position']
        events.append(e)

    pfs = frame['participantFrames']
    for p in pfs:
        if 'position' in pfs[p]:
            pfs[p]['x'] = pfs[p]['position']['x']
            pfs[p]['y'] = pfs[p]['position']['y']
            del pfs[p]['position']
        
        pfs[p]['timestamp'] = frame['timestamp']
        
        participantFrames.append(pfs[p])

eventFrame = pd.DataFrame(events)
eventFrame.to_csv("eventFrame.csv")

# partFrame = pd.DataFrame(participantFrames)
# # partFrame = partFrame.set_index('timestamp')
# partFrame.to_csv("partFrame.csv")


# p1Data = partFrame[partFrame.participantId == 1]
# p1Data.plot(x='timestamp', y='minionsKilled')



"""
DataFormat
Two Sheets
One for events one for participant frames

Events:
timestamp, type, participantId, itemId

Participant Frames
timestamp, currentGold, dominionScore, jungleMinionsKilled, level, minionsKilled, participantId, position, teamScore, totalGold, xp
# """
# with open("results.json", 'w') as outputFile:
#     outputFile.write(str(list(matchTimeline.find())))

# res = pd.DataFrame(list(matches.find()))

# participants = res['participants']


# print(res)