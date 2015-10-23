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

primes = [n for n in range(1000, 9999) if is_prime(n)]
result = []

k = len(primes)

for i in range(len(primes)):
    for j in range(i + 1, len(primes) - i):
        if 2 * primes[j] - primes[i] in primes:
            if sorted(str(primes[i])) == sorted(str(primes[j])) == sorted(str(2 * primes[j] - primes[i])):
                result.append([primes[i], primes[j], 2 * primes[j] - primes[i]])

print result

print "Finished in ", time.time() - start_time, "seconds"