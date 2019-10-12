#!/usr/bin/python3

from sys import stdin

for line in stdin:
    if 'problem' in line.lower():
        print('yes')
    else:
        print('no')
    