#!/usr/bin/env python3

def sieve(n):
	nums = [True for i in range(n)]
	p = 2
	while( p*p < n ):
		if nums[p]:
			for i in range(p*p, n, p):
				nums[i] = False
		p +=1

	primes = []
	for i in range(9,n):
		if nums[i]:
			primes.append(i)
	return primes

# The most important observation. We recognize that we're only dealing with prime factors of our number. Why?
# Let's say we find some base k for our number n. k can be either prime, or not. If k is not prime, then we
# can represent k in it's prime factorization. The prime factorizations of k are guaranteed to be smaller bases
# of n. The only things we need to be careful of are if the prime factorizations result in only 2s and 3s. So we 
# introduce next smallest bases that can solve that issue, (4, 6, and 9) into our set of possible bases. We then
# also add in bases 1, 2, and 3, because while these aren't valid bases, their partner factors are. We start our
# sieve at 11, so we also need to add the prime numbers 5 and 7 to be checked, and to round it out we just add 9
# as well so that we can use Python's range() function.
bases = list(range(1,10)) + sieve(int(2**(31/2))+1)

def solve(i):
	if i == 3:
		return 4
	val = i - 3
	if val < 4:
		return 0
	minOtherHalf = i
	for base in bases:
		if val%base == 0:
			if base > 3:
				# Here we've recognized that our list of possible factors is an increasing set, so the *first*
				# possible factor we find here is guaranteed the smallest of all factors
				return base 
			# We know that the base cannot be 1, 2, or 3, because they can never have a representation of our
			# decimal number ending in 3. (ie. remainer will never be 3) However, we still need to check their
			# pair partners. An observation of the other half is that as our possible factors increase, their
			# pairs will always decrease, so if we always overwrite minOtherHalf (at least until our possible
			# factors is greater than 4) then we'll always have the smallest partner factor.
			minOtherHalf = val//base
	return minOtherHalf


for n in map(int, iter(input, "0")):
	solution = solve(n)
	print(solution if solution else 'No such base')
