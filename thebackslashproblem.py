#!/usr/bin/env python3

from sys import exit

while True:
    try:
        n = int(input())
    except EOFError:
        exit()

    n = n if n == 1 else 2**n-1

    backslashes = '\\' * n

    sentence = list(input())

    for i in sentence:
        if ('!' <= i and i <= '*') or ('[' <= i and i <= ']'): print(backslashes, end='')
        print(i, end='')
    print()