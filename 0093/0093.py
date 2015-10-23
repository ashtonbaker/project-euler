import time
import operator
import itertools

def operate(num, ops):
	for i in range(1, len(num)):
		num[i] = ops[i-1](num[i-1], num[i])
	return num[-1]

def streak(t):

	t = sorted(t)
	result = 0

	for i in range(max(t) + 1):
		if t[i] == i + 1:
			result = i + 1
		else:
			break

	return result

start_time = time.time()
longest_streak = 0
longest_streak_combo = []
operations = [operator.add, operator.sub, operator.mul, operator.div]

for numset in itertools.combinations([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0], 4):
	targets = set([])
	for o in itertools.product(operations, repeat = 3):
	    for p in itertools.permutations([j for j in numset]):
	        t = operate([n for n in p], [k for k in o])
	        if t.is_integer() and t >= 1:
	            targets.add(int(t))

	s = streak([aln for aln in targets])

	if s > longest_streak:
		longest_streak = s
		longest_streak_combo = numset

print longest_streak_combo, longest_streak

print "Finished in ", time.time() - start_time, "seconds"