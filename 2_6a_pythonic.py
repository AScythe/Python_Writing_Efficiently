# pythonic code = idiomatic python
# most efficient and most readable
# several refactoring techniques to make it more pythonic

import geopy
# from mpl_toolkits.basemap import Basemap
import math
import json
import collections
import itertools
import numpy as np
# import matplotlib.pyplot as pp
# %matplotlib inline

import this  # the zen of python

medal = collections.namedtuple('medal', ['year', 'athlete', 'team', 'event'])
medals = [medal(*line.strip().split('\t'))
          for line in open('goldmedals.txt', 'r')]

athletes = []

for medal in medals:
    if medal.athlete not in athletes:  # if meet new athletes add to list
        athletes.append(medal.athlete)
athletes.sort()  # sort list
# print(athletes[:10])

# though no repitition clause calls for a set
athletes = sorted({medal.athlete for medal in medals})
print(athletes[:10])

winners_100m = {medal.athlete for medal in medals if '100m' in medal.event}
winners_200m = {medal.athlete for medal in medals if '200m' in medal.event}
# print(winners_100m)

# intersection of 2 sets
winners_both = {athlete for athlete in winners_100m if athlete in winners_200m}
# print(winners_both)
# OR
print(winners_100m & winners_200m)

# union of 2 sets
# print(winners_100m | winners_200m)

# difference of 2 sets
# print(winners_100m - winners_200m)


# inserting values in side strings
# standard: string interpolation method with percent operators
# for medal in medals:
#     if medal.event == 'long jump':
#         print('In %s, %s won for %s.' %
#               (medal.year, medal.athlete, medal.team))
# there is problem because there are long jump events only for men, and only for women
# to fix that:
# for medal in medals:
#     if medal.event.startswith('long jump'):
#         print('In %s, %s won for %s.' %
#               (medal.year, medal.athlete, medal.team))

# string format method
# replace placeholders with sequence numbers
for medal in medals:
    if medal.event.startswith('long jump'):
        # print('In {0}, {1} won for {2}.'.format(
        #     medal.year, medal.athlete, medal.team))
        print(f'In {medal.year}, {medal.athlete} won for {medal.team}.')

# use keyword syntax
# for medal in medals:
#     if medal.event.startswith('long jump'):
#         print('In {year}, {athlete} won for {team}.'.format(
#             year=medal.year, athlete=medal.athlete, team=medal.team))


# return list of medals with certain criteria
# def findmedal(year=None, team=None, event=None):
#     filtered = medals
#     if year is not None:
#         filtered = [medal for medal in filtered if medal.year == year]
#     if team is not None:
#         filtered = [medal for medal in filtered if medal.team == team]
#     if event is not None:
#         filtered = [medal for medal in filtered if medal.event == event]
#     return filtered


# print(findmedal(year='1896', team='USA'))


# refactored: use generic syntax/argument to specify keyword arguments
# **kwargs - dict of all keyword arguments that are passed to the function
# then iterate over key value pairs in the dict
# and filter the medals by that critereon
# or by checking for all criteria for every medal all at once
def findmedal(**kwargs):
    return [medal for medal in medals
            # if all(medal.key == value for key, value in kwargs.items())] # not legal because just a string
            if all(getattr(medal, key) == value for key, value in kwargs.items())]


# set critereon/criteria to return
print(findmedal(year='1896', team='USA'))
print(findmedal(athlete='Carl Lewis'))


# *args - for positional arguments which yields tuple
# can also be used together with key word arguments
def sumseveral(*args, multiplier=1.0):
    return multiplier * sum(args)


print(sumseveral(1, 2, 3, multiplier=10))
