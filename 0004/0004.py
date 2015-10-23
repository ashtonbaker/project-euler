"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 * 99.Find the largest
palindrome made from the product of two 3-digit numbers.
"""

factor1 = 0
factor2 = 0
top = 0

for i in xrange(100, 1000):
    for j in xrange(100,1000):
        product = i * j
        if (str(product) == str(product)[::-1]) and product > top:
            factor1 = i
            factor2 = j
            top = product

print('%i * %i = %i') % (factor1, factor2, top)
