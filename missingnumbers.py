#!/usr/bin/env python3

n = int(input())
nums = [*range(1, 201)]
i = 0
for _ in range(n):
    i = int(input())
    nums.remove(i)
nums = [*filter(lambda x: x <= i, nums)]
print(*nums if nums else 'good job', sep='\n' if nums else '')
