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

primes = []
for x in range(1, 1001):
    if is_prime(x):
        primes.append(x)

max_n = 0
max_period = 0

for n in primes:
    remainders_seen = [0]*n
    remainder = 1
    period = 0

    for i in range(n):
        
        remainder = 10 * remainder - n * ((10 * remainder) / n)
        
        if remainders_seen[remainder] > 0:
            period = i + 1 - remainders_seen[remainder]
            break
        else:
            remainders_seen[remainder] = i + 1

    if period > max_period:
        max_n = n
        max_period = period
        print "1 / %i has a recurring cycle of length %i" %(max_n, max_period)

print "Completed in ", time.time() - start_time