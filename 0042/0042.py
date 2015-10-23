import math
import time

start_time = time.time()

# Import the words from the text file
with open("./words.txt","r") as f:
    w = [s for s in f.read().replace('"','').split(',')]

result = 0

for word in w:
	t = 0

	# Calculate the total value (t) of the word
	for char in word:
		t += ord(char) - ord('A') + 1

	# Test whether t is a triangular number. If so, increment result.
	if (math.sqrt(8 * t + 1) % 1 == 0.0) & (math.sqrt(8 * t + 1) % 2 == 1):
		result += 1

print result

print "Finished in ", time.time() - start_time, "seconds"