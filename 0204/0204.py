import math
import time

start_time = time.time()

search_limit = 10**9
hamming_numbers = set([1])
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
current_row = set(primes)

while(1):
	#print len(hamming_numbers)
	new_row = set([])

	for n in current_row:
		hamming_numbers.add(n)
		for p in primes:
			if n * p <= search_limit:
				new_row.add(n * p)

	if len(new_row) == 0:
		break

	current_row = new_row

print len(hamming_numbers)

print "Finished in ", time.time() - start_time, "seconds"