import time
start_time = time.time()

def flip_and_add(n):
	return n + int(str(n)[::-1])

def is_palindrome(n):
	return (n == int(str(n)[::-1]))

def is_lychrel(n):
	k = flip_and_add(n)
	for i in range(50):
		if is_palindrome(k):
			return False
		else:
			k = flip_and_add(k)
	return True

result = 0

for i in range(1, 10001):
	if is_lychrel(i):
		result += 1

print result

print "Finished in ", time.time() - start_time, "seconds"