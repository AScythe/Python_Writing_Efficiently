import geopy
from mpl_toolkits.basemap import Basemap
import math
import json
import collections
import itertools
import numpy as np
import matplotlib.pyplot as pp
# %matplotlib inline

# comprehension - to run a loop within a single line of code
# and collect the results of the loop in a collection, such as a list, dict, set
# format: f(element) for element in iterator if condition(element)

# generators - shortcut to write functions that implement iterators

cities = []
years = []

for game in open('games.txt', 'r'):
    words = game.split()

    city = ' '.join(words[:-1])
    year = words[-1].strip('()')

    cities.append(city)
    years.append(year)

coordinates_by_city = json.load(open('coords.json', 'r'))
# print(coordinates_by_city)

# make list describing post ww2 olympic games
results = []

for city, year in zip(cities, years):
    if int(year) > 1945:
        results.append(city + ': ' + year)
# print(results[:10])

# list comprehension
results = [city + ': ' + year for city,
           year in zip(cities, years) if int(year) > 1945]
# print(results[:10])

# dict comprehension
cities_by_year = {year: city for city, year in zip(cities, years)}
# print(cities_by_year)

# set comprehension
# useful when we wish to collect each elements in a list/dict only once
cities_after_1945 = {city for year,
                     city in cities_by_year.items() if int(year) > 1945}
print(cities_after_1945)


# make a map given cities by year and coordinates by city
pp.figure(figsize=(8, 8))

world = Basemap(projection='ortho', lat_0=40, lon_0=0)

world.drawcoastlines(linewidth=0.25)
world.drawcountries(linewidth=0.25)

for year, city in cities_by_year.items():
    x, y = world(*coordinates_by_city[city])
# convert to map coordinates(x, y lat and long arguments)
# expand the tuple in the coordinates by city dict using * notation
# avoid warning when coordinates are outside the map,
# so x and y are returned as inf
    if not np.isinf(x) and not np.isinf(y):
        world.plot(x, y, 'r.')
        pp.text(x, y, year, fontsize=8, ha='center', va='bottom', color='navy')
pp.show()
