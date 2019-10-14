#!/usr/bin/env python3

from math import sqrt

R, B = map(int, input().split())

perimeter = R+4
area = R+B

L = int(max(1/2*((perimeter/2)+sqrt((perimeter/2)**2-4*area)),
            1/2*((perimeter/2)-sqrt((perimeter/2)**2-4*area))))
W = int(area/L)

print(L, W)
