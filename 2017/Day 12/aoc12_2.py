file = open("aoc12_input.txt")
l = file.read().split("\n")
file.close()

conn = {}
for desc in l:
	args = desc.replace(",", "").split()

	conn.update({int(args[0]): [int(j) for j in args[2:]]})

groups = 0
visited = set()
for start in range(len(l)):
	if start in visited:
		continue
	
	group = [start]
	groups += 1
	visited.add(start)
	i = 0
	while i < len(group):
		for j in conn[group[i]]:
			if j not in group:
				group.append(j)
				visited.add(j)
		i += 1

print(groups)