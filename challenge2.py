# challenge

import geopy
from mpl_toolkits.basemap import Basemap
import math
import json
import collections
import itertools
import numpy as np
import matplotlib.pyplot as pp
# %matplotlib inline


medal = collections.namedtuple('medal', ['year', 'athlete', 'team', 'event'])
medals = [medal(*line.strip().split('\t'))
          for line in open('goldmedals.txt', 'r')]

# finding athletes with most gold medals
medals_by_athlete = collections.Counter(medal.athlete for medal in medals)
print(medals_by_athlete.most_common(5))

# find althletes with medals in most events
# we have to collect events won by every athletes
events_by_athlete_set = collections.defaultdict(
    set)  # set to avoid repetition of events

for medal in medals:
    events_by_athlete_set[medal.athlete].add(medal.event)


def howmany(tup):
    return len(tup[1])


# reverse to make sure highest number is the beginning
# print(sorted(events_by_athlete_set.items(), key=howmany, reverse=True))

# but 100m and 100men (or 100m women) are counted as different events
# we need to clean that


def clean(event):
    return ' '.join(word for word in event.split() if word not in ('men', 'women'))


# print(clean('100m'))
# print(clean('100m men'))


events_by_athlete_set = collections.defaultdict(set)

for medal in medals:
    events_by_athlete_set[medal.athlete].add(clean(medal.event))


# def howmany(tup):
#     return len(tup[1])


print(sorted(events_by_athlete_set.items(), key=howmany, reverse=True))
# seems like long distance runners are the most versatile athletes followed by sprinters
