import math
import time

start_time = time.time()

def p(x, y):
	return (x**4 - y**4)/(x**3 + y**3)

a = 1
b = 1

print p(a, b)

print "Finished in {} seconds".format(time.time() - start_time)