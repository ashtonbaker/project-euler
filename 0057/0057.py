import math
import time

start_time = time.time()

numerator_memory = {0:3, 1:7}
denominator_memory = {0:2, 1:5}

def numerator(n):
	if not n in numerator_memory:
		numerator_memory[n] = 2 * numerator_memory[n - 1] + numerator_memory[n - 2]
	return numerator_memory[n]

def denominator(n):
	if not n in denominator_memory:
		denominator_memory[n] = 2 * denominator_memory[n - 1] + denominator_memory[n - 2]
	return denominator_memory[n]

count = 0

for i in range(1000):
	if len(str(numerator(i))) > len(str(denominator(i))):
		count += 1

print count

print "Finished in ", time.time() - start_time, "seconds"