"""
Project Euler
Problem 9
Special Pythagorean triplet

A Pytagorean triplet is a set of three natural numbers a < b < c for which
    a^2 + b^2 = c^2
There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find
The product a * b * c
"""

for n in xrange(1, 1000):
    for m in xrange(n + 1, 1000):
        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n**2
        if a + b + c == 1000:
            print(a)
            print(b)
            print(c)
            print(a * b * c)
