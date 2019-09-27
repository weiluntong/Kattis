#!/usr/bin/env python3


q = int(input())
primeFactors = set()

# While it's even we have prime factors of 2. So keep dividing.
while (q % 2 == 0):
    primeFactors.add(2)
    q /= 2

# Find the next prime factor i, starting at 3. Since the inner loop takes out all multiples of i, if q is divisible by i, then i is a prime factor.
for i in range(3, int(q**0.5)+1, 2):
    # While it's divisible by i, we need to keep dividing by i. This will take out all the multiples of i that are also factors of q.
    while(q % i == 0):
        primeFactors.add(i)
        q /= i

if (q > 2):
    primeFactors.add(q)

# if the set has more than 1 prime factor, then there exists factors p and m such that q=p^k*m^o rather than q=p^k
print('yes' if len(primeFactors) == 1 else 'no')
