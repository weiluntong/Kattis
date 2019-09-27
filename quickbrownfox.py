#!/usr/bin/env python3

n = int(input())

for i in range(n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    missing = []
    string = input().lower()
    for char in alphabet:
        if char not in string:
            missing.append(char)
    if len(missing):
        print('missing ' + ''.join(missing))
    else:
        print('pangram')
