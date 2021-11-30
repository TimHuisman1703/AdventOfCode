file = open("aoc06_input.txt")
l = file.read().split("\n")
file.close()

points = [tuple([int(k) for k in j.split(", ")]) for j in l]

width = height = 1
for p in points:
	width = max(width, p[0])
	height = max(height, p[1])

print(f"Width: {width}, Height: {height}")

points = [(j[0]+width, j[1]+height) for j in points]
g = [[-1 for _ in range(3*width)] for _ in range(3*height)]
queue = []

for i in range(len(points)):
	p = points[i]
	g[p[1]][p[0]] = i

	queue.append(p)

while 1:
	new_queue = []

	for p in queue:
		x, y = p
		id = g[y][x]
		
		for ix, iy in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
			if iy < 0 or iy > len(g)-1 or ix < 0 or ix > len(g[0])-1:
				continue

			if g[iy][ix] > -1:
				continue
			
			free = True
			
			for jx, jy in [(ix-1, iy), (ix+1, iy), (ix, iy-1), (ix, iy+1)]:
				if jy < 0 or jy > len(g)-1 or jx < 0 or jx > len(g[0])-1:
					continue

				if g[jy][jx] != -1 and g[jy][jx] != id:
					free = False
					break
			
			if free:
				if (ix, iy, id) not in new_queue:
					new_queue.append((ix, iy, id))
	
	queue = []
	for ix, iy, id in new_queue:
		g[iy][ix] = id
		queue.append((ix, iy))
	
	if not queue:
		break

	print(f"One iteration (Length: {len(queue)})")

non_infinite = [*range(len(points))]

for ix in range(len(g[0])):
	if g[0][ix] in non_infinite:
		non_infinite.remove(g[0][ix])
	if g[-1][ix] in non_infinite:
		non_infinite.remove(g[-1][ix])

for iy in range(len(g)):
	if g[iy][0] in non_infinite:
		non_infinite.remove(g[iy][0])
	if g[iy][-1] in non_infinite:
		non_infinite.remove(g[iy][-1])

areas = []

for id in non_infinite:
	areas.append(sum(row.count(id) for row in g))

print(max(areas))