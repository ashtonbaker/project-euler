spiral_size = 1001

total = 1
size = 3
n = 1
step = 2

while size <= spiral_size:
	for i in range(4):
		n += step
		total += n

	step += 2
	size += 2

print total