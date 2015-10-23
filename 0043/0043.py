import time
start_time = time.time()

def is_pandigital(n):
	return sorted([int(char) for char in str(n)]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

candidates = [[], [str(17*(6 + n)) for n in range(53)]]
primes = [1, 2, 3, 5, 7, 11, 13, 17]

for i in range(7):
	candidates[0] = candidates[1]
	candidates[1] = []
	for n in candidates[0]:
		for d in range(10):
			k = str(d) + n
			if (int(k[:3]) % primes[6 - i]) == 0:
				candidates[1].append(k)

candidates = [int(n) for n in candidates[1] if is_pandigital(n)]

print candidates
print sum(candidates)

print "Finished in ", time.time() - start_time, "seconds"