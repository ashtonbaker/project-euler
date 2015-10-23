import time
global math
import math
start_time = time.time()

def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def p(n):
	# returns the n-th pentagonal number
    return (n * (3 * n - 1)) / 2

def pentagonal_test(n):
	# tests whether n is pentagonal
	if is_square(24 * n + 1) and (int(math.sqrt(24 * n + 1)) % 6 == 5):
		return True
	else:
		return False

d = 2
m = 1
n = 1

while(1):
	m = 1
	n = 1

	while p(m) - p(n) < p(d):
		m += 1
		if p(m) - p(n) > p(d):
			n += 1
			m = n + 1

		if pentagonal_test(p(m) + p(n)) and pentagonal_test(p(m) - p(n)):
			result = p(d)
			break

	d += 1

print p(d)

print "Finished in ", time.time() - start_time, "seconds"