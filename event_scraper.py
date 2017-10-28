from bs4 import BeautifulSoup
from mechanize import Browser
# from firebase import firebase
from json import loads, dumps
from pprint import pprint

def getMetadata(url):
    browser = Browser()
    json = loads(browser.open(eventsJsonUrl).read())
    metadata = json['meta']
    return metadata

eventsJsonUrl = 'https://mediamagnet.osu.edu/api/v1/events.json'

allEvents = []
metadata = getMetadata(eventsJsonUrl)
link = metadata['links']['first']
pprint(metadata)

browser = Browser()
while link:
    print link
    json = browser.open(link).read()
    eventDict = loads(json)
    allEvents.extend(eventDict['events'])
    link = eventDict['meta']['links']['next']

print len(allEvents), 'events information found'

outFile = 'events_raw.json'
with open(outFile, 'w') as eventsFile:
    eventsFile.write(dumps(allEvents, indent=4, separators=(',', ': ')))
