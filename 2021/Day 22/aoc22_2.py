file = open("aoc22_input.txt")
l = file.read().split("\n")
file.close()

def diff_cube(c, d):
	cx, cy, cz = c
	dx, dy, dz = d
	if (cx[0] >= dx[1] or dx[0] >= cx[1]) \
		or (cy[0] >= dy[1] or dy[0] >= cy[1]) \
		or (cz[0] >= dz[1] or dz[0] >= cz[1]):
		return [c]
	
	cs = []
	if cx[0] < dx[0]:
		cs.append(((cx[0], dx[0]), (cy[0], cy[1]), (cz[0], cz[1])))
	if dx[1] < cx[1]:
		cs.append(((dx[1], cx[1]), (cy[0], cy[1]), (cz[0], cz[1])))
	
	min_x = max(cx[0], dx[0])
	max_x = min(cx[1], dx[1])

	if cy[0] < dy[0]:
		cs.append(((min_x, max_x), (cy[0], dy[0]), (cz[0], cz[1])))
	if dy[1] < cy[1]:
		cs.append(((min_x, max_x), (dy[1], cy[1]), (cz[0], cz[1])))
	
	min_y = max(cy[0], dy[0])
	max_y = min(cy[1], dy[1])

	if cz[0] < dz[0]:
		cs.append(((min_x, max_x), (min_y, max_y), (cz[0], dz[0])))
	if dz[1] < cz[1]:
		cs.append(((min_x, max_x), (min_y, max_y), (dz[1], cz[1])))
	
	return cs

cubes = []

for i in l:
	on, a = i.split()
	on = on == "on"
	x, y, z = a.split(",")
	min_x, max_x = [int(j) for j in x[2:].split("..")]
	min_y, max_y = [int(j) for j in y[2:].split("..")]
	min_z, max_z = [int(j) for j in z[2:].split("..")]
	
	d = ((min_x, max_x + 1), (min_y, max_y + 1), (min_z, max_z + 1))
	new_cubes = []

	for c in cubes:
		new_cubes.extend(diff_cube(c, d, on))
	cubes = new_cubes

	if on:
		cubes.append(d)

s = 0
for cx, cy, cz in cubes:
	s += (cx[1] - cx[0]) * (cy[1] - cy[0]) * (cz[1] - cz[0])

print(s)