beans = [0, 2, 1, 1, 1]

n = 1
hand = 0

while beans != [1] * 5:
	if hand == 0:
		hand = beans[n % 5]
		beans[n % 5] = 0
	else:
		hand -= 1
		beans[n % 5] += 1
	print beans
	n += 1

print n