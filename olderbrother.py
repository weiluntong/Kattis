#!/usr/bin/env python3


q = int(input())
primeFactors = set()

while (q % 2 == 0):
    primeFactors.add(2)
    q /= 2

for i in range(3, int(q**0.5)+1, 2):
    while(q % i == 0):
        primeFactors.add(i)
        q /= i

if (q > 2):
    primeFactors.add(q)

# if the set has more than 1 prime factor, then there exists factors p and m such that q=p*m rather than q=p^k
print('yes' if len(primeFactors) == 1 else 'no')
