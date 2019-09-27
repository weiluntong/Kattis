#!/usr/bin/env python3

for _ in range(int(input())):
    recording = list(input().split())
    for info in iter(input, 'what does the fox say?'):
        sound = info.split()[2]
        recording = list(filter(lambda x: x != sound, recording))
    print(*recording)
