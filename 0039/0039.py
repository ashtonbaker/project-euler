import time
start_time = time.time()

p = [0] * 1001

m = 2
n = 1
k = 0
a = 3
b = 4
c = 5

pythagorean_triples = []
perimeter = 12

while perimeter <= 1000:
    while perimeter <= 1000:
        while perimeter <= 1000:

            if not sorted([a, b, c]) in pythagorean_triples:
                pythagorean_triples.append(sorted([a, b, c]))

            k += 1
            a = k * (m ** 2 - n ** 2)
            b = k * 2 * m * n
            c = k * (m ** 2 + n ** 2)
            perimeter = a + b + c

        k = 1
        m += 1
        a = k * (m ** 2 - n ** 2)
        b = k * 2 * m * n
        c = k * (m ** 2 + n ** 2)
        perimeter = a + b + c

    k = 1
    n += 1
    m = n + 1
    a = k * (m ** 2 - n ** 2)
    b = k * 2 * m * n
    c = k * (m ** 2 + n ** 2)
    perimeter = a + b + c

for t in pythagorean_triples:
    p[t[0] + t[1] + t[2]] += 1

print p.index(max(p))


print "Finished in ", time.time() - start_time, "seconds"