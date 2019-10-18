#!/usr/bin/env python3

FBI = False

for i in range(5):
    blimp = input()
    if 'FBI' in blimp:
        print(i+1, end=' ')
        FBI = True

print('HE GOT AWAY!' if not FBI else '')