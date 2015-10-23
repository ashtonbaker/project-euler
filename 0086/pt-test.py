import time
import math

start_time = time.time()

def is_integer(x):
	return (abs(x - int(x)) < 0.000000000001)

solution_set = set([])

for i in range(1, 100):
	for j in range(1, 100):
		for k in range(1, 100):
			d1 = math.sqrt(k ** 2 + (i + j) ** 2)
			d2 = math.sqrt(i ** 2 + (j + k) ** 2)
			d3 = math.sqrt(j ** 2 + (i + k) ** 2)
			
			print sum([1 for n in [d1, d2, d3] if is_integer(n)]) >= 2

print "Finished in ", time.time() - start_time, "seconds"