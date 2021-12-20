file = open("aoc20_input.txt")
l = file.read().split("\n")
file.close()

STEPS = 2

min_x, max_x, min_y, max_y = 10*100, -10*100, 10*100, -10*100

a = l[0]
s = set()
for iy in range(len(l) - 2):
	for ix in range(len(l[iy+2])):
		if l[iy+2][ix] == "#":
			s.add((ix, iy))
			if ix < min_x:
				min_x = ix
			if ix + 1 > max_x:
				max_x = ix + 1
			if iy < min_y:
				min_y = iy
			if iy + 1 > max_y:
				max_y = iy + 1

for step in range(STEPS):
	min_x, max_x, min_y, max_y = min_x - 1, max_x + 1, min_y - 1, max_y + 1

	ns = set()
	for iy in range(min_y, max_y):
		for ix in range(min_x, max_x):
			i = 0
			for jy in range(iy - 1, iy + 2):
				for jx in range(ix - 1, ix + 2):
					i *= 2
					if (jx, jy) in s or (step % 2 == 1 and (jy < min_y + 1 or jy > max_y - 2 or jx < min_x + 1 or jx > max_x - 2)):
						i += 1
			if a[i] == "#":
				ns.add((ix, iy))
	s = ns

print(len(s))