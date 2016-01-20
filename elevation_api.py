__author__ = 'tai'

import sys
import simplejson
import urllib

start_point = sys.argv[1]
end_point = sys.argv[1]
key = sys.argv[1]

ELEVATION_BASE_URL = "https://maps.googleapis.com/maps/api/elevation/json"
url = ELEVATION_BASE_URL + '?locations=' + start_point + "," + end_point +'&key=AIzaSyCtsxFi2UFr6Cr4rWLFsviWXOvhEh1UEsk'
respond = urllib.urlopen(url)
#data = simplejson.loads(respond.read())
print respond['results']
#print data