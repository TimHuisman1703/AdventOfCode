file = open("aoc18_input.txt")
l = file.read().split("\n")
file.close()

STEPS = 10

w, h = len(l[0]), len(l)

g = [[0 for _ in range(w)] for _ in range(h)]

for iy in range(h):
	for ix in range(w):
		g[iy][ix] = ".|#".index(l[iy][ix])

for _ in range(STEPS):
	ng = [[0 for _ in range(w)] for _ in range(h)]

	for iy in range(h):
		for ix in range(w):
			n = [0] * 3
			for jy in range(max(0, iy - 1), min(h, iy + 2)):
				for jx in range(max(0, ix - 1), min(w, ix + 2)):
					n[g[jy][jx]] += 1
			
			if g[iy][ix] == 0:
				ng[iy][ix] = 1 if n[1] >= 3 else 0
			elif g[iy][ix] == 1:
				ng[iy][ix] = 2 if n[2] >= 3 else 1
			elif g[iy][ix] == 2:
				ng[iy][ix] = 2 if n[1] > 0 and n[2] > 1 else 0
	
	g = ng

n = [0] * 3
for iy in range(h):
	for ix in range(w):
		n[g[iy][ix]] += 1

print(n[1] * n[2])