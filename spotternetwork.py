import feedparser
import re

class SpotterNetwork:
  def __init__(self):
    self.locations = []

  def add_location(self, name, uid, location_datetime, latitude, longitude):
    in_hash = { 'name': name, 'uid': uid, 'time': location_datetime, \
                'latitude': latitude, 'longitude': longitude }
    self.locations.append(in_hash)

  def get_locations(self):
    return self.locations

  def load_entries(self, url = 'http://www.spotternetwork.org/feeds/rss-positions.xml'):
    feed = feedparser.parse(url)
    p_name = re.compile('\(Name\)([^\(]*)')
    p_email = re.compile('\(Name\)([^\(]*)')
    p_time = re.compile('\(Reported At\)([^\(]*)')

    for e in feed.entries:
      name = p_name.search(e.summary).group(1).strip()
      uid = e.id.split('=')[1]
      location_time = p_time.search(e.summary).group(1).strip()
      self.addLocation(name, uid, location_time, e.geo_lat, e.geo_long)

  def print_locations(self):
    for r in self.locations:
      print "Name: {}, ID: {}, Location: {},{}, Time: {}".format( \
          r['name'], r['uid'], r['latitude'], r['longitude'], \
          r['time'])

if __name__ == "__main__":
  locations = SpotterNetwork()
  locations.load_entries()
  locations.print_locations()
