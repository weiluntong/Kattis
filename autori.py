#!/usr/bin/env python3

print(*list(filter(lambda x: x.isupper(), list(input()))), sep='')