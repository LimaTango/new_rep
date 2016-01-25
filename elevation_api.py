_author__ = 'tai'

from matplotlib import pyplot as plt
import simplejson
import urllib
import numpy as np
# f = open('elevation_data.txt', 'w')

ELEVATION_BASE_URL = 'http://maps.google.com/maps/api/elevation/json?path='
key = '&key=AIzaSyCtsxFi2UFr6Cr4rWLFsviWXOvhEh1UEsk'


def get_elevation(path, samples):
    url = "https://maps.googleapis.com/maps/api/elevation/json?path=" + path + "&samples=400&key=AIzaSyCtsxFi2UFr6Cr4rWLFsviWXOvhEh1UEsk"
    response = simplejson.load(urllib.urlopen(url))
    elevation_array = []
    for result_set in response['results']:
        if result_set['elevation'] < 0:
            result_set['elevation'] = 0
        elevation_array.append(result_set['elevation'])
    print response["status"]
    return elevation_array

if __name__ == '__main__':
    elevation_list = []
    start_lat = "54.15,"
    end_lat = "54.55,"
    lng_list = np.linspace(18.46, 15.86, num=400)
    for elt in lng_list:
        lng = elt
        start_str = start_lat + str(lng)
        end_str = end_lat + str(lng)
        pathStr = start_str + "|" + end_str
        elevation = get_elevation(pathStr, "100")
        elevation_list.append(elevation)
    plt.imshow(elevation_list)
    plt.show()

