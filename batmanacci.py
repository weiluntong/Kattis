#!/usr/bin/env python3

from functools import lru_cache

@lru_cache()
def fib(n):
    if n==1 or n==2: return 1
    return fib(n-2)+fib(n-1)

n, k = map(int, input().split())

# Interesting observation here: Notice that k<=10**8, and fib grows (exponentially).
# What this means is that there will be a point x0 which for all x > x0, fib(x) >= k.
# Well, in our logic, we split our fib into two parts, fib(n-2) + fib(n-1). Depending
# on how large k is, we want to recurse into one of those parts and search for k in
# the new subset, and do this until we're left with whether k is N, or A. Interestingly
# enough, this means that there is a point at which we're always going to take the first
# half, because there is a point at which fib(x) >= k (recall all x > x0). What that
# means is we never half to calculate the second half of fib(x) because we never use it.
# This significantly reduces the total number of fib sequences we have to calculate.
# Which is required because Python is slow (its not necessary in C++ which handles
# recursion better). so we precompute what that point x0 is such that fib(x0) >= k.
# The brute force separate python script method just ran while fib(j) < k, and spat
# out j. This was 88. Give it a little leeway and we have 100.
n = min(n, 100)

while n > 2:
    l = fib(n-2)
    if k > l:
        k = k - l
        n -= 1
    else:
        n -= 2

print('N' if n == 1 else 'A')