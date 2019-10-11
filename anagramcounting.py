#!/usr/bin/env python3

from functools import lru_cache, reduce
from collections import Counter

@lru_cache()
def factorial(num):
    if num <= 1: 
        return 1
    else: 
        return num * factorial(num-1) 

def EOFinput(*a, **kw):
    try:
        return input(*a, **kw)
    except EOFError:
        return None

for i in iter(EOFinput, None):
    ans = factorial(len(i)) // reduce(lambda x, y: x*y, map(factorial, Counter(i).values()))
    for j in Counter(i).values(): ans //= factorial(j)
    print(ans)