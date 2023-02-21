fruits = ["apple", "banana", "cherry"]

import itertools
import functools

def update(d, l):
    d[l] = d.setdefault(l, 0) + 1
    return d

letters = itertools.chain(*((l for l in f) for f in fruits))
frequency = functools.reduce(update, letters, {})
print(max((v,k) for k,v in frequency.items()))
