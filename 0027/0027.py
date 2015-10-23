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

best_a = 0
best_b = 0
max_run = 0

primes_up_to_1000 = []
for x in range(1, 1001):
    if is_prime(x):
        primes_up_to_1000.append(x)

for a in range(-999, 1000):
    for b in primes_up_to_1000:

        print a, b

        n = 1

        while is_prime(n ** 2 + a * n + b):
            if n > max_run:
                max_run = n
                best_a = a
                best_b = b
            n += 1

print best_a, best_b
print best_a * best_b
print max_run