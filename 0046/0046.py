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
    #print '\t',f
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

n = 21

while True:
  i = 0
  while is_prime(n - 2 * i ** 2) == False:
    if n - 2 * i ** 2 < 0:
      print n
      exit()
    i += 1

  n += 2

print "Finished in ", time.time() - start_time, "seconds"