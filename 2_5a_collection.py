# python collections module offers several more objects

import geopy
from mpl_toolkits.basemap import Basemap
import math
import json
import collections
import itertools
import numpy as np
import matplotlib.pyplot as pp
# %matplotlib inline

# tabular data separted by tabs \t
f = open('goldmedals.txt', 'r').readlines()[:10]
# print(f)

# namedtuple - similar on a dict for a list, this is a dict for a tuple
# you don't like to change sensitive data like medals
# fixed set of keys, and values cannot be changed once namedtuple is created
medal = collections.namedtuple('medal', ['year', 'athlete', 'team', 'event'])
# instance of named tuple is initialized
m = medal('1896', 'Thomas Burke', 'USA', '100m men')
# print(m)
# unlike dict, fields are accessed by a "." notation
# print(m.year, m.athlete)

medals = [medal(*line.split('\t')) for line in open('goldmedals.txt', 'r')]
# use "*" notation to spread the list of words across the arguments of that medal constructor
# print(medals[:5])

# get rid of new line at each record
medals = [medal(*line.strip().split('\t'))
          for line in open('goldmedals.txt', 'r')]
# print(medals[:5])

# let's start counting medals
teams = collections.Counter(medal.team for medal in medals)
# print(teams)
# ZZX - mixed teams which is common in earlier olympics
print(teams.most_common(5))


def best_by_year(year):
    counts = collections.Counter(
        medal.team for medal in medals if medal.year == str(year))
    best = counts.most_common(5)

    return [b[0] for b in best], [b[1] for b in best]


print(best_by_year(1900))


# # plot the top 5 best countries in 1990
# countries, tally = best_by_year(1900)

# pp.figure(figsize=(6, 3))

# bars = pp.bar(np.arange(5), tally, align='center')
# pp.xticks(np.arange(5), countries)

# pp.show()

# # plot best 5 countries in 3 years
pp.style.use('ggplot')

colors = pp.cm.Set3(np.linspace(0, 1, 5))


def plotyear(year):
    countries, tally = best_by_year(year)

    bars = pp.bar(np.arange(5), tally, align='center')
    pp.xticks(np.arange(5), countries)

    for bar, color in zip(bars, colors):
        bar.set_color(color)

    pp.title(year)


pp.figure(figsize=(4, 6))

pp.subplot(3, 1, 1)
plotyear(2008)
pp.subplot(3, 1, 2)
plotyear(2012)
pp.subplot(3, 1, 3)
plotyear(2016)

pp.tight_layout()

pp.show()

# Collection defaultdict targets the common use case
# where we're modifying key value pairs in a dictionary,
# but we need special handling for the first time that we see a key.
# For instance, making a list of all medal winners for each country.
winners_by_country = {}

for medal in medals:
    if medal.team not in winners_by_country:
        winners_by_country[medal.team] = [medal.athlete]
    else:
        winners_by_country[medal.team].append(medal.athlete)

# print(winners_by_country['ITA'])
# but this is repetitive

# What we need is Collections defaultdict.
# It's sole argument is a factory function
# that returns the default value of each dictionary item.
# In this case, the factory will be list,
# which when called without arguments, returns an empty list.
winners_by_country = collections.defaultdict(list)

for medal in medals:
    winners_by_country[medal.team].append(medal.athlete)

# print(winners_by_country['FRA'])


# Collections OrderedDict
# like a regular dict but remembers the insertion order
ordered_winners = collections.OrderedDict()

for medal in medals:
    if medal.team == 'ITA':
        ordered_winners[medal.athlete] = medal.event + ' ' + medal.year

# print(ordered_winners)

# print({medal.athlete: medal.event + ' ' +
#        medal.year for medal in medals if medal.team == 'ITA'})


# Collection deque
dq = collections.deque(range(10))
print(dq)

for i in range(10, 15):
    dq.append(i)  # add 10 at the end
    v = dq.popleft()  # remove element at the start
    print(dq)

for i in reversed(range(0, 5)):
    dq.appendleft(i)  # add 4 at the start
    v = dq.pop()  # remove element at the end
    print(dq)
