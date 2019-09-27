#!/usr/bin/env python3

def adjAreWater(l, r, c, n, m):
    top = '#' if r-1 < 0 else l[r-1][c]
    bottom = '#' if r+1 >= n else l[r+1][c]
    left = '#' if c-1 < 0 else l[r][c-1]
    right = '#' if c+1 >= m else l[r][c+1]
    if top == bottom and bottom == left and left == right and right == '#':
        return True
    return False

n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(list(input()))

for rowC, row in enumerate(l):
    for tileC, tile in enumerate(row):
        if tile != '#' and (rowC % 2 == tileC %2 or adjAreWater(l, rowC, tileC, n, m)):
            l[rowC][tileC] = 'E'

for line in l:
    print(''.join(line))
