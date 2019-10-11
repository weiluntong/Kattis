#!/usr/bin/env python3


def bfs(neighborsOf, inDegrees):
    isTrapped = []
    queue = []
    # Find all dead ends. All cities with zero of these reversed in degrees
    # are dead ends. If no dead ends exist at the very beginning, then every
    # city has somewhere our MoM can run to in this graph.
    for i in inDegrees:
        if not inDegrees[i]:
            queue.append(i)
    while (queue):
        city = queue.pop(0)
        isTrapped.append(city)
        for neighbor in neighborsOf[city]:
            inDegrees[neighbor] -= 1
            # If this neighbor reached zero of these reversed in degrees then
            # it only had a one way ticket to a city that we know is trapped
            # so we know this one is a dead end too and we need to check which
            # cities have a one way ticket to this neighbor. So we add it to
            # the queue to check its neighbors.
            if not inDegrees[neighbor]:
                queue.append(neighbor)
    return isTrapped


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
    # We're gonna do something novel here. We're gonna traverse this graph backwards.
    # Logic: If there is a city that MoM can get trapped in, then it won't have any out
    # degrees so we flip our in and out degrees so that "trapped" cities all have 0 in
    # degrees.
    adj[d].append(o)
    if o not in inDegrees:
        inDegrees[o] = 0
    if d not in inDegrees:
        inDegrees[d] = 0
    inDegrees[o] += 1
trapped = bfs(adj, inDegrees)
for i in iter(input2, None):
    if i in trapped:
        print(i, 'trapped')
    else:
        print(i, 'safe')
