file = open("aoc11_input.txt")
g = [[int(j) for j in row] for row in file.read().split("\n")]
file.close()

STEPS = 100

c = 0

for _ in range(STEPS):
	changed = True
	while changed:
		changed = False

		for iy in range(len(g)):
			for ix in range(len(g[0])):
				if g[iy][ix] >= 9:
					for jy in range(max(0, iy-1), min(len(g), iy+2)):
						for jx in range(max(0, ix-1), min(len(g[0]), ix+2)):
							g[jy][jx] += 1
					
					changed = True
					g[iy][ix] = -1000000000
		
	for iy in range(len(g)):
		for ix in range(len(g[0])):
			if g[iy][ix] < 0:
				c += 1
				g[iy][ix] = -1
			g[iy][ix] += 1

print(c)