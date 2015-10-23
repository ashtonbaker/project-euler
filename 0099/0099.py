import math
import time

start_time = time.time()

# Import the lines of the triangle from the text file
with open("./base_exp.txt","r") as f:
    lines = [s for s in f.read().split('\n')]

lines = [[int(n) for n in lines[k].split(',')] for k in range(len(lines))]

max = 0
n = 1
max_n = 1

for l in lines:
	x = l[1] * math.log(l[0])
	if x > max:
		max = x
		max_n = n
	n += 1

print max_n

print "Finished in ", time.time() - start_time, "seconds"