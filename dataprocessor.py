import pandas as pd
from matplotlib import pyplot

partFrame = pd.read_csv("partFrame.csv")

p1Data = partFrame[partFrame.participantId == 1]
p1Data['cs'] = p1Data['minionsKilled'] + p1Data['jungleMinionsKilled']
p1Data.plot(x='timestamp', y='cs')

pyplot.show()