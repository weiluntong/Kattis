#!/usr/bin/env python3


def dfs(node, neighborsOf, visited):
    if visited[node]:
        return
    visited[node] = True
    for neighbor in neighborsOf[node]:
        dfs(neighbor, neighborsOf, visited)


for _ in range(int(input())):
    m = int(input())
    grid = [[] for j in range(m)]
    count = 0
    for i in range(int(input())):
        x, y = map(int, input().split())
        grid[x].append(y)
        grid[y].append(x)
        visited = [False for j in range(m)]
        dfs(0, grid, visited)
        for i in range(m):
            if visited:
                continue
            count += 1
            dfs(i, grid, visited)
    print(count)
