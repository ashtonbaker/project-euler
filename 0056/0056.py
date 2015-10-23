max_digit_sum = 0
max_a = 0
max_b = 0

for a in range(1,101):
	for b in range(1, 101):
		n = 0
		for digit in str(a ** b):
			n += int(digit)
		if n >= max_digit_sum:
			max_digit_sum = n
			max_a = a
			max_b = b

print max_a, '^', max_b, '=', max_a ** max_b
print max_digit_sum