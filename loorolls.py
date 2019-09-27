#!/usr/bin/python3

l, n = map(int, input().split())
ans = 1
while True:
    k = l % n
    if k == 0:
        break
    n = n-k
    ans += 1
print(ans)