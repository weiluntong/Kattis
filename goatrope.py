#!/usr/bin/python3


import math

def hypot(x, y):
    return math.sqrt(x**2 + y**2)

userIn = input().split()
x = int(userIn[0])
y = int(userIn[1])
x1 = int(userIn[2])
y1 = int(userIn[3])
x2 = int(userIn[4])
y2 = int(userIn[5])

d = 0
if x > x1 and x < x2 and y > y2:
    d = y - y2
elif x > x2 and y > y2:
    d = hypot(x - x2, y - y2)
elif x > x2 and y > y1 and y < y2:
    d = x - x2
elif (x > x2 and y < y1):
    d = hypot(x - x2, y1 - y)
elif (x > x1 and x < x2 and y < y1):
    d = y1 - y
elif (x < x1 and y < y1):
    d = hypot(x1 - x, y1 - y)
elif x < x1 and y > y1 and y < y2:
    d = x1 - x
elif x < x1 and y > y2:
    d = hypot(x1 - x, y - y2)

print(d)
