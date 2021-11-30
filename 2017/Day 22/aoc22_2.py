file = open("aoc22_input.txt")
l = file.read().split("\n")
file.close()

ITERATIONS = 10000000

infected = set()
weakened = set()
flagged = set()
width, height = len(l[0]), len(l)
for iy in range(height):
	for ix in range(width):
		if l[iy][ix] == "#":
			infected.add((ix, iy))

x, y = width // 2, height // 2
dir = (0, -1)

c = 0

for iter in range(ITERATIONS):
	if (x, y) in weakened:
		weakened.remove((x, y))
		infected.add((x, y))
		c += 1
	elif (x, y) in infected:
		dir = (-dir[1], dir[0])
		infected.remove((x, y))
		flagged.add((x, y))
	elif (x, y) in flagged:
		dir = (-dir[0], -dir[1])
		flagged.remove((x, y))
	else:
		dir = (dir[1], -dir[0])
		weakened.add((x, y))
	
	x += dir[0]
	y += dir[1]

	if iter % 1000000 == 999999:
		print(f"Passed {iter + 1}")

print(c)