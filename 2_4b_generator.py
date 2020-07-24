import geopy
# from mpl_toolkits.basemap import Basemap
import math
import json
import collections
import itertools
import numpy as np
# import matplotlib.pyplot as pp
# %matplotlib inline

# generator expressions
# just replace brackets/braces with parenthesis from comprehensions
# then assign result to a variable
# in some cases you may not need to save the results of a comprehension in the list
# instead you may want to consume them immediately

even = (i for i in range(20) if i % 2 == 0)
print(even)  # this is an iterator object, not a list

# you can iterate it using __next__() to obtain element in the sequence
# print(even.__next__())
# print(even.__next__())
# etc

print(sum(even))  # get sum, even without constructing the list


def fibonacci():
    f1, f2 = 0, 1

    while True:
        yield f2
        f1, f2 = f2, f1 + f2
        # this is an infinite sequence and will not terminate


f = fibonacci()

# generators are regular functions that contains special keyword yield

results = [next(f) for i in range(20)]
# next(f) shorthand for f.__next__()
print(results)

# when this generator is called their execution is suspended
# and they return an iterator object which can be given to a for loop or use in a list comprehension
# when the next is called on the resulted iterator the execution of the function is resumed
# until it reaches the yield statement, that values is then passed back to the caller
