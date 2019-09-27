#!/usr/bin/env python3

input()
k = list(map(int, input().split()))
expenses = 0

for i in k:
    if i < 0:
        expenses += i

print(abs(expenses))
