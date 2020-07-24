import geopy
# from mpl_toolkits.basemap import Basemap
import math
import json
import collections
import itertools
import numpy as np
# import matplotlib.pyplot as pp
# %matplotlib inline

# for n in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]:
#     print(n)

# for l in "Fibonacci":
#     print(l)

# iterator - python object that defines the item __next__()
# __next__() is called repeatedly and stop iteration with the StopIteration exception

# it = iter("Fib")
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

# parse content of file line by line
# open - open file
# r - for reading
for game in open('games.txt', 'r'):
    print(game, end='')

# for game in open('games.txt', 'r'):
#     city = game.split()[0] # split - split lines with spaces
#     year = game.split()[1]
#     print(city, year)
#     # there is a problem in strings seperated with space

# for game in open('games.txt', 'r'):
#     words = game.split()
#     city = ' '.join(words[:-1])  # join - join words with spaces
#     year = words[-1].strip('()')  # strip - remove () from the years
#     print(city, year)

cities, years = [], []

for game in open('games.txt', 'r'):
    words = game.split()

    city = ' '.join(words[:-1])
    year = words[-1].strip('()')

    cities.append(city)
    years.append(year)
