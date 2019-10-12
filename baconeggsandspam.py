#!/usr/bin/python3

while True:
    i = int(input())
    if i == 0:
        break
    orders = {}
    for j in range(i):
        order = (input()).split()
        name = order[0]
        for k in range(1, len(order)):
            item = order[k]
            if item not in orders:
                orders.update({item : []})
            orders[item].append(name)
    for l in sorted(orders):
        print(l, end=' ')
        for m in sorted(orders[l]):
            print(m, end=' ')
        print()
    print()
    