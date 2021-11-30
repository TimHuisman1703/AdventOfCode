file = open("aoc17_input.txt")
l = file.read().split("\n")
file.close()

def get_neighbors(g, x, y, z):
	c = 0
	for dz in range(-1, 2):
		if z+dz < 0 or z+dz > len(g)-1:
			continue
		for dy in range(-1, 2):
			if y+dy < 0 or y+dy > len(g[0])-1:
				continue
			for dx in range(-1, 2):
				if x+dx < 0 or x+dx > len(g[0][0])-1:
					continue
				if dx == dy == dz == 0:
					continue
				if g[z+dz][y+dy][x+dx]:
					c += 1
	return c

def print_field(g, cycles_left):
	cycles_left += 1
	print("-"*100)
	mz = (len(g)-1)//2
	for iz in range(cycles_left, len(g)-cycles_left):
		print(f"z = {iz-mz}")
		for iy in range(cycles_left, len(g[0])-cycles_left):
			for ix in range(cycles_left, len(g[0][0])-cycles_left):
				print("#" if g[iz][iy][ix] else ".", end = "")
			print("")

cycles = 6
dim_x = 2*cycles+2+len(l[0])
dim_y = 2*cycles+2+len(l)
dim_z = 2*cycles+2+1
g = [[[0 for ix in range(dim_x)] for iy in range(dim_y)] for iz in range(dim_z)]

for iy in range(len(l)):
	for ix in range(len(l[0])):
		g[(dim_z-1)//2][cycles+1+iy][cycles+1+ix] = int(l[iy][ix] == "#")

for i in range(cycles):
	print_field(g, cycles-i)
	n = [[[0 for ix in range(dim_x)] for iy in range(dim_y)] for iz in range(dim_z)]
	for iz in range(dim_z):
		for iy in range(dim_y):
			for ix in range(dim_x):
				p = get_neighbors(g, ix, iy, iz)
				if p == 2:
					n[iz][iy][ix] = g[iz][iy][ix]
				elif p == 3:
					n[iz][iy][ix] = 1
	g = n
print_field(g, 0)
print(sum(sum(sum(ix) for ix in iy) for iy in g))