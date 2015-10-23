import math
import time

start_time = time.time()

total = 0

for n in range(1, 101):
	for r in range(1, n + 1):
		if math.factorial(n) / (math.factorial(r) * math.factorial(n - r)) > 1000000:
			total += 1
			print n, r

print total

print "Finished in ", time.time() - start_time, "seconds"



