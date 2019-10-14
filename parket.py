#!/usr/bin/env python3

from math import sqrt

R, B = map(int, input().split())

perimeter = R+4
area = R+B

L = int(max(1/4*(perimeter+sqrt(perimeter*perimeter-16*area)),
            1/4*(perimeter-sqrt(perimeter*perimeter-16*area))))

W = int(area/L)

print(L, W)
