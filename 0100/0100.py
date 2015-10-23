import math
import time

start_time = time.time()

def blue(n):
	if n == 0:
		return 1
	elif n == 1:
		return 3
	else:
		return 6 * blue(n - 1) - blue(n - 2) - 2

def red(n):
	b = blue(n)
	return int(math.sqrt(8*b**2 - 8*b + 1)-2*b+1)/2

n = 0

while blue(n) + red(n) < 10 ** 12:
	n += 1

print blue(n)

print "Finished in {} seconds".format(time.time() - start_time)