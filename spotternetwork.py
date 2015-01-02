"""Module for converting spotternetwork kml to geojson

When running from command line will dump geojson of spotternetwork positions
"""

from pykml import parser
from geojson import Feature, FeatureCollection, Point
from geojson import dumps as geojsondumps
import urllib2

class SpotterNetwork(object):
    """Convert spotternetwork positions from kml to geojson

    Attributes:
        positions (geojson.feature.FeatureCollection): Feature collection
            containing positions of spotters.  positions is not defined in the
            __init__ method because the geojson library will not create an
            empty FeatureCollection object.
    """
    def __init__(self):
        """Nothing to see here"""
        pass

    def dump_positions(self):
        """Print geojson featurecollection object as a string"""
        print geojsondumps(self.positions)

    def get_positions(self):
        """Return geojson featurecollectin object"""
        return self.positions

    def load_from_kml(self,
                      url='http://www.spotternetwork.org/feeds/earth-all.txt'):
        """Parse kml positions and create geojson FeatureCollection

        Connect to spotter network url that has spotternetwork positions in kml
        format and create a a FeatureCollection containing the positions of
        each spotter.  The url for the kml data has extension txt which is
        strange but using the url with the kml extension which references the
        txt url doesn't seem to work with the pykml library.
        """
        locations = []
        kml_object = urllib2.urlopen(url)
        kml_root = parser.parse(kml_object).getroot()
        placemarks = kml_root.Folder.getchildren()
        for place in placemarks:
            position = Feature()
            feature_properties = {}
            feature_properties['sn_id'] = place.attrib['id']
            feature_properties['name'] = place.name.text
            description = self.__parse_kml_description(place.description.text)
            feature_properties.update(description)
            lon, lat, alt = place.Point.getchildren()[0].text.split(',')
            point = Point((float(lon), float(lat)))
            position.update(properties=feature_properties, geometry=point)
            locations.append(position)
        # Cannot create an empty FeatureCollection so must create instance
        # variable here.  Yucky
        self.positions = FeatureCollection(locations)

    def __parse_kml_description(self, desc):
        """Parse kml description line and return dictionary of data

        The description line in the kml contains semi structured data that will
        be turned into structured data inside the geojson feature object.

        Args:
            desc: String containing description

        Returns:
            dictionary containing structured description data
        """
        fields = ['phone', 'email', 'ham', 'note', 'time']
        desc_map = {}
        desc_list = desc.split('<br>')
        # There is always an extra <br> remove last empty item
        desc_list.pop(-1)
        if desc_list[0] == 'Active':
            desc_map['status'] = True
        else:
            desc_map['status'] = False
        # Now that we have status out of the way remove from list
        # Everything else needs to be split on ': ' (colon space)
        desc_list.pop(0)
        for item in desc_list:
            key, value = item.split(': ', 1)
            key = key.lower()
            # Don't do anything for name, already have that
            if key == 'name':
                continue
            # Change position time to time
            if key == 'position time':
                key = 'time'
            desc_map.update({key: value})
        # Add None for missing keys
        for item in fields:
            if item not in desc_map:
                desc_map.update({item: None})
        return desc_map

class StormReport(object):
    """Placeholder for storm reports"""
    def __init__(self):
        pass

if __name__ == "__main__":
    spotters = SpotterNetwork()
    spotters.load_from_kml()
    spotters.dump_positions()
