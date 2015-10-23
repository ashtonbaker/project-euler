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

def anonymize_numbers(n, digit_indices):
    result = list(str(n))

    for i in digit_indices:
        if i < len(result): 
            result[i] = '*'

    return "".join(result)


primes = set([])

for x in xrange(1000):#(56993, 1000000):
    if is_prime(x):
        primes.add(x)

c = [bin(n)[2::][::-1] for n in range(2**6)]
c = [[i for i, letter in enumerate(s) if letter == '1'] for s in c]

for digit_indices in c:

    anonymized_numbers = [anonymize_numbers(p, digit_indices) for p in primes]

    n = max(set(anonymized_numbers), key=anonymized_numbers.count)
    print n, anonymized_numbers.count(n)
