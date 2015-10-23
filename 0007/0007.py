"""
Project Euler
Problem 7
10001st prime

By listing the first six prime numbers: 2, 3, 5, 6, 11, 13, we can see that the
6th prime is 13. What is the 10001st prime number?
"""

import math
primes = [i for i in xrange(1000000)]
for n in xrange(2,1000):
    for i in xrange(2*n,len(primes),n):
        primes[i] = 0
primes = filter(lambda a: a != 0, primes)
print(primes[10001])
