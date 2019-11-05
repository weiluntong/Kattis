#!/usr/bin/env python3

X, N = int(input()), int(input())
sum = X

for _ in range(N):
    P = int(input())
    sum += X - P
print(sum)
