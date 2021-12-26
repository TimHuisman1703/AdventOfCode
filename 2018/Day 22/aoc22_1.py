file = open("aoc22_input.txt")
l = file.read().split("\n")
file.close()

depth = int(l[0].split()[-1])
tx, ty = [int(j) for j in l[1].split()[-1].split(",")]

g = [[0 for _ in range(tx + 1)] for _ in range(ty + 1)]

s = 0
for iy in range(ty + 1):
	for ix in range(tx + 1):
		if iy == 0:
			geo = ix * 16807
		elif ix == 0:
			geo = iy * 48271
		elif ix == tx and iy == ty:
			geo = 0
		else:
			geo = g[iy-1][ix] * g[iy][ix-1]
		
		g[iy][ix] = (geo + depth) % 20183
		s += g[iy][ix] % 3

print(s)