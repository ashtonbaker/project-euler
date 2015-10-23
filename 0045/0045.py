import time
start_time = time.time()

def triangular(n):
    return n * (n + 1) / 2

def pentagonal(n):
	return n * (3 * n - 1) / 2

def hexagonal(n):
	return n * (2 * n - 1)

i = 2
j = 2
k = 2

while True:
	t = triangular(i)
	p = pentagonal(j)
	h = hexagonal(k)
	m = min([t,p,h])

	if (t == p) & (t == h):
		print "T(%i) = P(%i) = H(%i) = %i" % (i, j, k, t)
		if raw_input("Continue [Y/N]: ") == 'N':
			break
		else:
			i += 1
	elif t == m:
		i += 1
	elif p == m:
		j += 1
	else:
		k += 1

print "Finished in ", time.time() - start_time, "seconds"