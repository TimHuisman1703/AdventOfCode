file = open("aoc15_input.txt")
l = file.read().split("\n")
file.close()

g = [[-1 for _ in range(len(l[0]))] for _ in range(len(l))]
units = []

elfs = set()


i = 0
for iy in range(len(g)):
	for ix in range(len(g[0])):
		if l[iy][ix] == "#":
			g[iy][ix] = -2
		elif l[iy][ix] in "GE":
			g[iy][ix] = i
			units.append(["GE".index(l[iy][ix]), 200])
			i += 1

print(*g, sep="\n")
print(units)