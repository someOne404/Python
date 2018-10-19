import urllib.request
import math
import webbrowser

key = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/wendys.csv')
print(key)

wendys_lat = []
wendys_lon = []
distances = []
addresses = []

for line in key:
    text_line = line.decode('utf-8')
    no_newline = text_line.strip()
    row = no_newline.split(',')
    lat = float(row[0])
    wendys_lat.append(lat)
    lon = float(row[1])
    wendys_lon.append(lon)


def distance_between(lat_1, lon_1, lat_2, lon_2):
    '''Uses the "great circle distance" formula and the circumference of the earth
    to convert two GPS coordinates to the miles separating them'''
    lat_1, lon_1 = math.radians(lat_1), math.radians(lon_1)
    lat_2, lon_2 = math.radians(lat_2), math.radians(lon_2)
    theta = lon_1 - lon_2
    dist = math.sin(lat_1)*math.sin(lat_2) + math.cos(lat_1)*math.cos(lat_2)*math.cos(theta)
    dist = math.acos(dist)
    dist = math.degrees(dist)
    dist = dist * 69.06         # 69.09 = circumference of earth in miles / 360 degrees

    return dist
