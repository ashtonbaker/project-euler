import time

start_time = time.time()

for n in xrange(1010101030,1389026625, 100):
	if str(n ** 2)[::2] == '1234567890':
		print n,'^', 2, '=', n ** 2 
		break

	n += 40
	if str(n ** 2)[::2] == '1234567890':
		print n,'^', 2, '=', n ** 2 
		break

print "Finished in ", time.time() - start_time, "seconds"

