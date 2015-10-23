import time
start_time = time.time()

base_10_palindromes = []
sum = 0

for i in range(1, 1000):
    n = str(i)
    base_10_palindromes.append(int(n + n[::-1]))
    base_10_palindromes.append(int(n + n[::-1][1::]))

for n in base_10_palindromes:
    if bin(n)[2::] == bin(n)[2::][::-1]:
        sum += n
        print n, bin(n)[2::]

print sum

print "Finished in ", time.time() - start_time, "seconds"