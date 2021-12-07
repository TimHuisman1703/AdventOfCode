file = open("aoc10_input.txt")
l = file.read().split("\n")
file.close()

asteroids = set()
for iy in range(len(l)):
	for ix in range(len(l[0])):
		if l[iy][ix] == "#":
			asteroids.add((ix, iy))

best = 0
for a in asteroids:
	left = set()
	right = set()
	up = down = 0
	for b in asteroids:
		if b[0] < a[0]:
			left.add((b[1] - a[1]) / (b[0] - a[0]))
		elif b[0] > a[0]:
			right.add((b[1] - a[1]) / (b[0] - a[0]))
		elif b[1] < a[1]:
			up = 1
		elif b[1] > a[1]:
			down = 1
	
	score = len(left) + len(right) + up + down
	best = max(best, score)

print(best)