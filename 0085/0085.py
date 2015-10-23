import time
start_time = time.time()

def number_of_rectangles(m, n):
	return (m * n) * (m*n + n + m + 1) / 4

best_solution_distance = 2000000
best_solution_dimensions = 0

i = 0

while number_of_rectangles(i, i) < 2000000:

	i += 1
	m = i
	n = i

	current_solution_distance = abs(number_of_rectangles(m, n) - 2000000)

	if current_solution_distance < best_solution_distance:
		best_solution_distance = current_solution_distance
		best_solution_dimensions = m * n

	while number_of_rectangles(m, n) < 2000000:
		m += 1
		current_solution_distance = abs(number_of_rectangles(m, n) - 2000000)
		if current_solution_distance < best_solution_distance:
			best_solution_distance = current_solution_distance
			best_solution_dimensions = m * n

print best_solution_dimensions
print best_solution_distance

print "Finished in ", time.time() - start_time, "seconds"