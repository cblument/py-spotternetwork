import feedparser
import re
p_name = re.compile('\(Name\)([^\(]*)')
p_email = re.compile('\(Name\)([^\(]*)')
p_time = re.compile('\(Reported At\)([^\(]*)')

sn_feed_url = 'http://www.spotternetwork.org/feeds/rss-positions.xml'

feed = feedparser.parse(sn_feed_url)

for e in feed.entries:
  name = p_name.search(e.summary).group(1).strip()
  uid = e.id.split('=')[1]
  report_time = p_time.search(e.summary).group(1).strip()
  print "Lat: {}, Lon: {}, Name: {} ID: {}, Time: {}".format(e.geo_lat, e.geo_long, name, uid, report_time)
