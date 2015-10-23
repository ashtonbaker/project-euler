import time
import math
import itertools

start_time = time.time()

def distance(a, b):
	return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def is_pythagorean(a, b, c):
	d = sorted([distance(a, b), distance(a, c), distance(b, c)])
	if abs(d[0]**2 + d[1]**2 - d[2]**2) < 0.000001:
		return True
	else:
		return False

count = 0

points = [[x, y] for y in range(51) for x in range(51)][1:]
print points

print len(points)

for i in range(2600):
	for j in range(i + 1, 2600):
		if is_pythagorean(points[i], points[j], [0, 0]):
			count += 1

print count

print "Finished in ", time.time() - start_time, "seconds"