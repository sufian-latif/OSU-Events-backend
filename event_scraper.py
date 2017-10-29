import urllib.request
from json import loads, dumps
from pprint import pprint
from time import strptime

eventsJsonUrl = 'https://mediamagnet.osu.edu/api/v1/events.json'
json = loads(urllib.request.urlopen(eventsJsonUrl).read())
metadata = json['meta']

allEvents = []
link = metadata['links']['first']
pprint(metadata)

while link:
    print(link)
    json = urllib.request.urlopen(link).read()
    eventDict = loads(json)
    allEvents.extend(eventDict['events'])
    link = eventDict['meta']['links']['next']

print(len(allEvents), 'events information found')

outFile = 'events_raw.json'
timeFormat = '%Y-%m-%d %H:%M:%S %z'
with open(outFile, 'w') as fout:
    fout.write(dumps(sorted(allEvents, key=lambda event: strptime(event['start_date'], timeFormat)),
                     indent=4, separators=(',', ': ')))
