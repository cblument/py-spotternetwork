import feedparser
import re

class spotternetwork:
  def __init__(self):
    self.locations = []

  def addLocation(self, name, uid, location_datetime, latitude, longitude):
    in_hash = { 'name': name, 'uid': uid, 'time': location_datetime, \
                'latitude': latitude, 'longitude': longitude }
    self.locations.append(in_hash)

  def getLocations(self):
    return self.locations

  def loadFromUrl(self, url = 'http://www.spotternetwork.org/feeds/rss-positions.xml'):
    feed = feedparser.parse(url)
    p_name = re.compile('\(Name\)([^\(]*)')
    p_email = re.compile('\(Name\)([^\(]*)')
    p_time = re.compile('\(Reported At\)([^\(]*)')

    for e in feed.entries:
      name = p_name.search(e.summary).group(1).strip()
      uid = e.id.split('=')[1]
      location_time = p_time.search(e.summary).group(1).strip()
      self.addLocation(name, uid, location_time, e.geo_lat, e.geo_long)

  def printLocations(self):
    for r in self.locations:
      print "Name: {}, ID: {}, Location: {},{}, Time: {}".format( \
          r['name'], r['uid'], r['latitude'], r['longitude'], \
          r['time'])

if __name__ == "__main__":
  locations = spotternetwork()
  locations.loadFromUrl()
  locations.printLocations()
