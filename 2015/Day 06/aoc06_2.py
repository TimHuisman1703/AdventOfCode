file = open("aoc06_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

g = [[0 for ix in range(1000)] for iy in range(1000)]

for i in l:
	s = i[5:].split()
	x1, y1 = [int(j) for j in s[1].split(",")]
	x2, y2 = [int(j) for j in s[3].split(",")]

	if i[6] == "n":
		for iy in range(y1, y2+1):
			for ix in range(x1, x2+1):
				g[iy][ix] += 1
	elif i[6] == "f":
		for iy in range(y1, y2+1):
			for ix in range(x1, x2+1):
				g[iy][ix] = max(0, g[iy][ix]-1)
	else:
		for iy in range(y1, y2+1):
			for ix in range(x1, x2+1):
				g[iy][ix] += 2

print(sum(sum(iy) for iy in g))