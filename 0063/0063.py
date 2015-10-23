import math
import time

start_time = time.time()


count = 0

for n in range(1, 21):
	top = math.floor( (10 ** n - 1) ** (1.0 / float(n)) ) 
	bottom = math.ceil( (10 ** (n - 1)) ** (1.0 / float(n)) )
	print n, bottom, top
	count += top - bottom + 1

print count

print "Finished in ", time.time() - start_time, "seconds"