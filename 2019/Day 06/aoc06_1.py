file = open("aoc06_input.txt")
l = file.read().split("\n")
file.close()

s = [(0, "COM")]
children = {}

for i in l:
	a, b = i.split(")")

	if a not in children.keys():
		children[a] = set()
	children[a].add(b)
	
	if b not in children.keys():
		children[b] = set()

c = 0
while len(s):
	orbits, curr = s.pop()
	c += orbits
	
	for i in children[curr]:
		s.append((orbits + 1, i))

print(c)