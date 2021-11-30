file = open("aoc22_input.txt")
l = file.read().split("\n")
file.close()

ITERATIONS = 10000

infected = set()
width, height = len(l[0]), len(l)
for iy in range(height):
	for ix in range(width):
		if l[iy][ix] == "#":
			infected.add((ix, iy))

x, y = width // 2, height // 2
dir = (0, -1)

c = 0

for iter in range(ITERATIONS):
	if (x, y) in infected:
		dir = (-dir[1], dir[0])
		infected.remove((x, y))
	else:
		dir = (dir[1], -dir[0])
		infected.add((x, y))
		c += 1
	
	x += dir[0]
	y += dir[1]

print(c)