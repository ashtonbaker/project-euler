import math
import time

start_time = time.time()

# Import the lines of the triangle from the text file
with open("./keylog.txt","r") as f:
    combs = [int(s) for s in f.read().split('\n') if s != '']

print combs

print "Finished in ", time.time() - start_time, "seconds"