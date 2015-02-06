"""
Project Euler
Problem 10
Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million
"""

import math
primes = [i for i in xrange(11)]
primes[1] = 0
for n in xrange(2,1500):
    for i in xrange(2*n,len(primes),n):
        primes[i] = 0
# primes = filter(lambda a: a != 0, primes)

print(sum(primes))
