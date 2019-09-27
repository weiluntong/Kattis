#!/usr/bin/env python3

# from math import gcd

for i in iter(input, '0 0'):
    num, denom = map(int, i.split())
    remainder = num % denom
    # reducer = gcd(remainder, denom) if remainder > 0 else 1
    # remainder //= reducer
    # denom //= reducer
    print(str(num // denom) + ' ' + str(remainder) + ' / ' + str(denom))

# NOTE: commented code is for reduced mixed fractions. Just for funsies.
