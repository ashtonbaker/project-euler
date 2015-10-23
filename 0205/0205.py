import time
import itertools

start_time = time.time()

peter = [0] * 36
colin = [0] * 36

# Count how many ways Peter and Colin can get each sum from 1 to 36

for n in [sum(x) for x in itertools.product(range(1,5),repeat=9)]:
	peter[n - 1] += 1

for n in [sum(x) for x in itertools.product(range(1,7),repeat=6)]:
	colin[n - 1] += 1

# Calculate the probability for each player to get each score

peter = [n / float(262144) for n in peter]
colin = [n / float(46656) for n in colin]

print round(sum([colin[n] * sum(peter[(n + 1):]) for n in range(35)]),7)

print "Finished in ", time.time() - start_time, "seconds"