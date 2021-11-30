file = open("aoc07_input.txt")
l = file.read().split("\n")
file.close()

programs = set()
children = set()

for s in l:
	args = s.replace(",", "").split()

	programs.add(args[0])
	children = children.union(set(args[3:]))

print(*(programs - children))