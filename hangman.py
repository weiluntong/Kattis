#!/usr/bin/python3

word = input()
perm = input()
result = 'WIN'
count = 0

for letter in perm:
    if letter not in word:
        count = count + 1
    else:
        word = word.replace(letter, '')
    if not word:
        break;
    elif count >= 10:
        result = 'LOSE'
print(result)