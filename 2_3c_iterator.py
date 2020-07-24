import geopy
import math
import json
import collections
import itertools
import numpy as np

cities, years = [], []

for game in open('games.txt', 'r'):
    words = game.split()

    city = ' '.join(words[:-1])
    year = words[-1].strip('()')

    cities.append(city)
    years.append(year)

# iterators

# # enumerate - iterate over tuples of an item and its ordinal number
# for i, city in enumerate(cities[:10]):
#     print(i, city)

# # sorted - iterate sorted list
# for city in sorted(cities[:10]):
#     print(city)

# # sort by known trigger criteria (key function) such as length of string
# for city in sorted(cities[:10], key=len):
#     print(city)

# # reverse - reverse iterator can be used to enumerate or sort, etc
# # compare with enumerate to see effect
# for i, city in enumerate(reversed(cities[:10])):
#     print(i, city)

# zip - iterate a joined multiple iterators or sequences
for year, city in zip(years[:10], cities):
    print(year, city)

# other iterators
# 1) map and filter - are special iterators that apply functions
# to all elements returned by an iterator
# either return the result or use it to select a subset of a sequence
# 2) Concatenate: itertools.chain(iter1, iter2)
# chain 2 iterators
# 3) Duplicate: i1, i2 = itertools.tee(iter,2)
# you make a copy

# if you are iterating over a numeric sequence you can do sum, product
# 4) Running Sum: itertools.accumulate(iter)
# 5) Element-by-element product: itertools.product(iter1, iter2)

# 6) Permutations: itertools.permutatations(string)
# 7) Combinations: itertools.combinations(string)
