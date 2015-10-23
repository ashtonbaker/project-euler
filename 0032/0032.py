import math
import time

start_time = time.time()

# Use a set for the results so that duplicate answers are automatically excluded
results = set([])

# Check for results A * B = C where A has 1 digit and B has 4 digits
for a in range(1, 10):
	for b in range(1234, 10000):
		c = a * b
		if sorted(str(a) + str(b) + str(c)) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
			print '%i * %i = %i' %(a, b, c)
			results.add(c)

# Check for results A * B = C where A has 2 digits and B has 3 digits
for a in range(12, 99):
	for b in range(123, 988):
		c = a * b
		if sorted(str(a) + str(b) + str(c)) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
			print '%i * %i = %i' %(a, b, c)
			results.add(c)

print sum(results)

print "Finished in ", time.time() - start_time, "seconds"