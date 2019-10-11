#!/usr/bin/env python3

def dfs(node, neighborsOf, visited):
    if visited[node]: return
    visited[node] = True
    for neighbor in neighborsOf[node]:
        dfs(neighbor, neighborsOf, visited)

for _ in range(int(input())):
    n, m, l = map(int, input().split())
    adj = [[] for _i in range(n+1)]
    for _edge in range(m):
        x, y = map(int, input().split())
        adj[x].append(y)
    visited = [False for _i in range(n+1)]
    for _start in range(l):
        start = int(input())
        dfs(start, adj, visited)

    print(len(list(filter(lambda x: x, visited))))