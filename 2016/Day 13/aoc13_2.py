file = open("aoc13_input.txt")
n = int(file.read())
file.close()

is_wall = {(1, 1): False}
came_from = {(1, 1): -1}

def check_wall(x, y):
	global is_wall

	if (x, y) in is_wall.keys():
		return is_wall[(x, y)]
	
	b = x*x + 3*x + 2*x*y + y + y*y + n
	wall = (bin(b).count("1") % 2) == 1

	is_wall.update({(x, y): wall})
	return wall

queue = [(1, 1, 0)]

r = 0
while True:
	x, y, cost = queue.pop(0)

	if cost > 50:
		break
	
	r += 1

	for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
		ix, iy = x + dx, y + dy

		if ix < 0 or iy < 0:
			continue

		if (ix, iy) not in came_from.keys():
			if not check_wall(ix, iy):
				came_from.update({(ix, iy): (x, y)})
				queue.append((ix, iy, cost+1))

print(r)