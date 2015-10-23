import math
import time

start_time = time.time()

bouncy = 0
non_bouncy = 1

n = 1

while bouncy / float(bouncy + non_bouncy) != 0.99:
	n += 1

	digits = [d for d in str(n)]
	sorted_digits = sorted(digits)
	reversed_digits = digits[::-1]

	if (digits == sorted_digits) or (reversed_digits == sorted_digits):
		non_bouncy += 1
	else:
		bouncy += 1

print n

print "Finished in ", time.time() - start_time, "seconds"