import geopy
from mpl_toolkits.basemap import Basemap
import math
import json
import collections
import itertools
import numpy as np
import matplotlib.pyplot as pp
# %matplotlib inline

# how to use basemap:
# https://basemaptutorial.readthedocs.io/en/latest/first_map.html

cities, years = [], []

for game in open('games.txt', 'r'):
    words = game.split()

    city = ' '.join(words[:-1])
    year = words[-1].strip('()')

    cities.append(city)
    years.append(year)

geolocator = geopy.geocoders.Nominatim(user_agent='programming-efficiently')
# geolocator - webservice that converts place descriptions to coordinates
# geopy - offers geolocator service
# Nominatem - geolocator object
# geopy.geocoders.Nominatim should be called with  unique user_agent to avoid user-policy violations.
# on a slow connection it is necessary to give Nominatim a higher timeout (e.g. timeout = 10)

locations = {}
for city in cities:
    print("Locating", city)
    locations[city] = geolocator.geocode(
        city.split('/')[0])  # handle special cases

print(locations["Paris"])

# draw a map using basemap of mathplotlib
pp.figure(figsize=(10, 5))

world = Basemap()
world.drawcoastlines(linewidth=0.25)
world.drawcountries(linewidth=0.25)


for city, pos in locations.items():
    world.plot(pos.longitude, pos.latitude, 'r.', markersize=10, latlon=True)
# # r. - red dots as markers

print(locations)
pp.show()

# after locating, the locations of rome and athens are wrong
# we need to specifically fix it

locations['Rome'] = geolocator.geocode('Rome, Italy')
locations['Athens'] = geolocator.geocode('Athens, Greece')
# check
print(locations['Rome'])
print(locations['Athens'])
