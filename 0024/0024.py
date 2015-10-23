import math

factorials = [math.factorial(i) for i in xrange(9, -1, -1)]

coefficients = [0] * 10
n = 0

while sum([a*b  for a,b in zip(factorials, coefficients)]) != 999999:

    while sum([a*b  for a,b in zip(factorials, coefficients)]) < 999999:
        coefficients[n] += 1

    if sum([a*b  for a,b in zip(factorials, coefficients)]) > 999999:
        coefficients[n] -= 1

    n += 1

permutation = []
available_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for c in coefficients:
	permutation.append(available_digits[c])
	del available_digits[c]

print ''.join(map(str, permutation))