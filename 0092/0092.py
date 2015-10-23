import math
import time

start_time = time.time()

one_set = set([1])
eightynine_set = set([89])

for n in xrange(1, 10000001):

	k = n	

	while 1:
		k = sum([int(d)**2 for d in str(k)])

		if k in one_set:
			one_set.add(n)
			break

		if k in eightynine_set:
			eightynine_set.add(n)
			break

print len(eightynine_set)

print "Finished in ", time.time() - start_time, "seconds"