file = open("aoc10_input.txt")
l = file.read().split("\n")
file.close()

cost = 0
for s in l:
	stack = []
	
	for c in s:
		if c in "([{<":
			stack += ["([{<".index(c)]
		if c in ")]}>":
			if stack and stack[-1] == ")]}>".index(c):
				stack = stack[:-1]
			else:
				cost += [3, 57, 1197, 25137][")]}>".index(c)]
				break

print(cost)