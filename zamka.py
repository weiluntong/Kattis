#!/usr/bin/env python3


def digitSum(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r


L, D, X = map(int, [input() for _ in range(3)])
numList = []
for i in range(L, D+1):
    if digitSum(i) == X:
        numList.append(i)

x = numList.pop(0)
y = numList.pop() if numList else x
print(x, y, sep='\n')
