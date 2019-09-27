#!/usr/bin/env python3

x, y, n = map(int, input().split())

for i in range(1, n+1):
    if not i % x:
        print('Fizz', end='')
    if not i % y:
        print('Buzz', end='')
    if i % x and i % y:
        print(i, end='')
    print()
