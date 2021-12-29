file = open("aoc23_input.txt")
l = file.read().split("\n")
file.close()

bots = []

for i in l:
	pos, r = i.split()
	x, y, z, _ = pos.split(",")
	x, y, z = int(x[5:]), int(y), int(z[:-1])
	r = int(r[2:])
	bots.append((x, y, z, r))

best = min(bots, key=lambda x: -x[3])

c = 0
for b in bots:
	if abs(b[0] - best[0]) + abs(b[1] - best[1]) + abs(b[2] - best[2]) <= best[3]:
		c += 1

print(c)