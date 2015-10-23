def digits(n):
	return [int(char) for char in str(n)]

solution = 0

for n in range(6 * 9**5):
	if n == sum([d ** 5 for d in digits(n)]):
		solution += n

print solution