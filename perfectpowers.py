#!/usr/bin/python3

import math

def get_greatest_power(x):
    i = 2
    neg = (x < 0)
    x = abs(x)
    while True:
        result = math.log(x)/math.log(i)
        if (abs(result - int(result)) < 0.00000001):
            if i ** (int(result)) == x:
                if neg and (int(result) % 2) == 0:
                    i += 1
                    continue
                return int(result);
        i = i+1
        if result <= 2:
            break
    return 1


while True:
    x = int(input())
    if x == 0:
        break;
    print(get_greatest_power(x))

