#!/usr/bin/env python3

def smallest(n):
    strNum = ''
    while n > 11:
        if n == 17: break
        strNum += '8'
        n -= 7
    if n == 17:
        strNum += '002'
    if n == 11:
        strNum += '02'
    if n == 10:
        strNum += '22'
    if n == 9:
        strNum += '81'
    if n == 8:
        strNum += '01'
    elif n == 7:
        strNum += '8'
    elif n == 6:
        strNum += '6'
    elif n == 5:
        strNum += '2'
    elif n == 4:
        strNum += '4'
    elif n == 3:
        strNum += '7'
    elif n == 2:
        strNum += '1'
    return strNum

test = int(input())

for t in range(test):
    n = int(input())
    # print(str(n)+" ", end = ' ')

    print(smallest(n)[::-1], end=' ')

    if n%2:
        print('7', end='')
        for i in range(1, (n-1)//2):
            print('1', end='')
    else:
        for i in range(n//2):
            print('1', end='')
    print()
