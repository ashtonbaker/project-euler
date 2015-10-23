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

def rotation(n, k):
    num = str(n)
    for i in range(k):
        num = num[1:] + num[0]
    return int(num)

primes = set([])
circular_primes = []

for i in range(1000000):
    if is_prime(i):
        primes.add(i)

for i in primes:
    print i
    all_prime = True
    for j in range(6):
        if not (rotation(i, j) in primes):
            all_prime = False

    if all_prime:
        circular_primes.append(i)

print circular_primes
print len(circular_primes)

