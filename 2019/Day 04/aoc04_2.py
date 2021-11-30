file = open("aoc04_input.txt")
a, b = [int(j) for j in file.read().split("-")]
file.close()

c = 0
for i in range(a, b+1):
	digits = [int(j) for j in str(i)]

	last = 0
	ascending = True
	for d in digits:
		if last > d:
			ascending = False
			break
		last = d
	
	if not ascending:
		continue
	
	double = False
	for d in set(digits):
		if digits.count(d) == 2:
			double = True
			break
	
	if double:
		c += 1

print(c)