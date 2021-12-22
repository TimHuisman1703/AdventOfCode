file = open("aoc22_input.txt")
l = file.read().split("\n")
file.close()

cubes = []

for i in l[:20]:
	on, a = i.split()
	on = on == "on"
	x, y, z = a.split(",")
	min_x, max_x = [int(j) for j in x[2:].split("..")]
	min_y, max_y = [int(j) for j in y[2:].split("..")]
	min_z, max_z = [int(j) for j in z[2:].split("..")]

	cubes.append((on, (min_x, max_x + 1), (min_y, max_y + 1), (min_z, max_z + 1)))

s = 0
for iz in range(-50, 51):
	print(f"iz = {iz}")
	for iy in range(-50, 51):
		for ix in range(-50, 51):
			state = False
			for on, cx, cy, cz in cubes:
				if cx[0] <= ix < cx[1] and cy[0] <= iy < cy[1] and cz[0] <= iz < cz[1]:
					state = on
			s += state

print(s)