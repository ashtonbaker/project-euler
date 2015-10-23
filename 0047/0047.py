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

primes = set([2, 3, 5, 7, 11, 13, 17])
max_prime = 15
run = 0
n = 18

while run < 4:
    n += 1
    if n % 2 == 1:
        if is_prime(n):
            primes.add(n)
            max_prime = n
            run = 0
            n += 1

    prime_divisors = 0

    for p in primes:
        if n % p == 0:
            prime_divisors += 1

    if prime_divisors >= 4:
        run += 1
    else:
        run = 0

print n - 3, n - 2, n - 1, n
print "Finished in ", time.time() - start_time, "seconds"