import time
import math

start_time = time.time()

results = []

for k in range(10000):
	n = 1
	concatenated_product = ''
	while len(concatenated_product) < 9:
		concatenated_product += str(k * n)
		n += 1

	if sorted(concatenated_product) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
		results.append(concatenated_product)
		print concatenated_product, k

print max(results)

print "Finished in ", time.time() - start_time, "seconds"