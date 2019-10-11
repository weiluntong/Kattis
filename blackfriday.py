#!/usr/bin/env python3

def solve(rolls):
    diceCount = [0 for _ in range(7)]
    for roll in rolls:
        diceCount[roll] += 1
    best = 0
    for index, num in enumerate(diceCount):
        if num == 1: best = index
    return best

input()
rolls=list(map(int, input().split()))
highest = solve(rolls)
position = 'none'
for index, roll in enumerate(rolls):
    if roll == highest:
        position = index + 1

print(position)
