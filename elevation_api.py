_author__ = 'tai'

from matplotlib import pyplot as plt
import matplotlib.mlab as ml
import simplejson
import urllib
import numpy as np
f = open('elevation_data.txt', 'w')

ELEVATION_BASE_URL = 'http://maps.google.com/maps/api/elevation/json'


def get_elevation(path="36.64,-116.83171|36.24,-116.83171", samples="100", sensor="false", **elvtn_args):
    elvtn_args.update({
        'path': path,
        'samples': samples,
        'sensor': sensor
    })
    url = ELEVATION_BASE_URL + '?' + urllib.urlencode(elvtn_args)
    response = simplejson.load(urllib.urlopen(url))
    elevation_array = []
    for result_set in response['results']:
        elevation_array.append(result_set['elevation'])
        #f.write(str(result_set['elevation']) + '\n')
    return elevation_array

if __name__ == '__main__':

    #startStr = raw_input('Enter the start latitude,longitude value (default Mt. Whitney) --> ').replace(' ','')
    #if not startStr:
    # startStr = "36.578581,-118.291994"

    #endStr = raw_input('Enter the end latitude,longitude value (default Death Valley) --> ').replace(' ','')
    #if not endStr:
    # endStr = "36.23998,-116.83171"
    elevation_list = []
    start_lat = "51.8836,"
    end_lat = "52.0836,"
    for i in range(30):
        longitude = 15.4 + 0.001*i
        start_str = start_lat + str(longitude)
        end_str = end_lat + str(longitude)
        pathStr = start_str + "|" + end_str
        elevation = get_elevation(pathStr, 30)
        elevation_list.append(elevation)
    long_list = np.linspace(15.4, 15.8, num=30)
    lat_list = np.linspace(51.8836, 52.0836, num=30)
    X, Y = np.meshgrid(long_list, lat_list)
    print len(elevation_list[0]), len(X), len(Y)
    #plt.contour(X, Y, elevation_list)
    plt.contour(np.array(elevation_list))
    plt.show()
