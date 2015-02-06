"""
Project Euler
Problem 17
Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total. If all the numbers
from 1 to 1000 (one thousand) inclusive were written out in words, how many
letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
"""

ones = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4,
        3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
tens = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]

sum = 0

for n in xrange(1, 1000):
    hundredsplace = n / 100
    sum += ones[hundredsplace]

    if n % 100 < 20:
        sum += ones[n % 100]
    else:
        onesplace = n % 10
        tensplace = (n % 100)/ 10
        sum += ones[onesplace]
        sum += tens[tensplace]

    if n % 100 > 0 and n >= 100:
        sum += 3

    if n >= 100:
        sum += 7

sum += 11

print sum
