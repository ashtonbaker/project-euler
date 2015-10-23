import time
start_time = time.time()

n = 1
finished = False

while not finished:
	if sorted(str(n)) == sorted(str(2 * n)) == sorted(str(3 * n)) == sorted(str(4 * n)) == sorted(str(5 * n)) == sorted(str(6 * n)):
		finished = True
	else:
		n += 1

print n
print "Finished in ", time.time() - start_time, "seconds"