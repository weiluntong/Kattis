#!/usr/bin/env python3


def detectCycle(node, neighborsOf, inDegrees):
    inDegreesHere = inDegrees.copy()
    queue = []
    queue.append(node)
    while (queue):
        city = queue.pop(0)
        if inDegreesHere[city] == -1:
            return True
        for neighbor in neighborsOf[city]:
            inDegreesHere[neighbor] -= 1
            queue.append(neighbor)
    return False


def input2(*a, **kw):
    try:
        return input(*a, **kw)
    except EOFError:
        return None


n = int(input())

adj = {}
inDegrees = {}
for _ in range(n):
    o, d = input().split()
    if o not in adj:
        adj[o] = []
    if d not in adj:
        adj[d] = []
    adj[o].append(d)
    if o not in inDegrees:
        inDegrees[o] = 0
    if d not in inDegrees:
        inDegrees[d] = 0
    inDegrees[d] += 1
for i in iter(input2, None):
    safe = detectCycle(i, adj, inDegrees)
    print(i, end=' ')
    print('safe' if safe else 'trapped')
