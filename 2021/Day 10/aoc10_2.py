file = open("aoc10_input.txt")
l = file.read().split("\n")
file.close()

scores = []

for s in l:
	stack = []
	
	for c in s:
		if c in "([{<":
			stack += ["([{<".index(c)]
		if c in ")]}>":
			if stack and stack[-1] == ")]}>".index(c):
				stack = stack[:-1]
			else:
				break
	else:
		curr = 0
		for c in stack[::-1]:
			curr = curr * 5 + (c + 1)
		scores += [curr]

scores = sorted(scores)
print(scores[len(scores) // 2])