file = open("aoc25_input.txt")
l = file.read().split("\n")
file.close()

height = len(l)
width = len(l[0])

east = set()
south = set()
for iy in range(height):
	for ix in range(width):
		if l[iy][ix] == ">":
			east.add((ix, iy))
		elif l[iy][ix] == "v":
			south.add((ix, iy))

steps = 0
moved = True
while moved:
	steps += 1
	moved = False
	
	new_east = set(east)
	new_south = set(south)
	for p in east:
		q = ((p[0] + 1) % width, p[1])
		if not q in east and not q in south:
			moved = True
			new_east.add(q)
			new_east.remove(p)
	for p in south:
		q = (p[0], (p[1] + 1) % height)
		if not q in new_east and not q in south:
			moved = True
			new_south.add(q)
			new_south.remove(p)
	
	east = new_east
	south = new_south

print(steps)