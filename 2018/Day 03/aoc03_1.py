file = open("aoc03_input.txt")
l = file.read().split("\n")
file.close()

c = 0
g = [[0 for _ in range(1000)] for _ in range(1000)]

for s in l:
	args = s.split()

	x, y = [int(j) for j in args[2][:-1].split(",")]
	w, h = [int(j) for j in args[3].split("x")]
	
	for iy in range(y, y+h):
		for ix in range(x, x+w):
			if g[iy][ix] == 1:
				c += 1
			g[iy][ix] += 1

print(c)