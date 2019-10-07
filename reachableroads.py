#!/usr/bin/env python3

def dfs(node, neighborsOf, visited):
    if visited[node]:
        return
    visited[node] = True
    for neighbor in neighborsOf[node]:
        dfs(neighbor, neighborsOf, visited)

def bfs(node, neighborsOf, visited):
    queue = []
    queue.append(node)
    visited[node] = True
    while queue:
        node = queue.pop(0)
        for neighbor in neighborsOf[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True


for _ in range(int(input())):
    m = int(input())
    grid = [[] for j in range(m)]
    count = -1
    for i in range(int(input())):
        x, y = map(int, input().split())
        grid[x].append(y)
        grid[y].append(x)
        
    visited = [False for j in range(m)]
    for i in range(m):
        if visited[i]:
            continue
        count += 1
        dfs(i, grid, visited)
    print(count)
