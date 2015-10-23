import math
import time

start_time = time.time()

# Import the lines of the triangle from the text file
with open("./triangle.txt","r") as f:
    triangle = [s for s in f.read().split('\n')]

triangle = [[int(n) for n in triangle[k].split()] for k in range(len(triangle))]

rows = len(triangle)

for n in range(1, rows):
    columns = len(triangle[n])
    for p in range(columns):
        if p == 0:
            triangle[n][p] += triangle[n - 1][p]
        elif p == range(columns)[-1]:
            triangle[n][p] += triangle[n - 1][p - 1]
        else:
            triangle[n][p] += max(triangle[n - 1][p],triangle[n - 1][p - 1])

print max(triangle[-1])

print "Finished in ", time.time() - start_time, "seconds"