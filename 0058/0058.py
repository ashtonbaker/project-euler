import time

start_time = time.time()

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

ratio = 1
n = 1
p = 0
d = 1

while ratio > 0.1:
	n += 2
	d += 4
	for i in range(4):
		k = n ** 2 - i * (n  - 1)
		if is_prime(k):
			p += 1
	ratio = float(p) / float(d)

print n, ratio

print "Finished in ", time.time() - start_time, "seconds"