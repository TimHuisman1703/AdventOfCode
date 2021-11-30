file = open("aoc08_input.txt")
l = file.read().split("\n")
file.close()

width = 50
height = 6

g = [[0]*width for j in range(height)]

for instr in l:
	args = instr.split()

	if args[0] == "rect":
		a, b = [int(j) for j in args[1].split("x")]

		for ix in range(a):
			for iy in range(b):
				g[iy][ix] = 1
	
	if args[1] == "row":
		a, b = int(args[2].split("=")[1]), int(args[4])

		new_row = [0]*width
		for ix in range(width):
			new_row[ix] = g[a][(ix - b) % width]
		
		g[a] = new_row
	
	if args[1] == "column":
		a, b = int(args[2].split("=")[1]), int(args[4])

		new_col = [0]*height
		for iy in range(height):
			new_col[iy] = g[(iy - b) % height][a]
		
		for iy in range(height):
			g[iy][a] = new_col[iy]
	
print("\n".join(["".join([".#"[tile] for tile in row]) for row in g]))
print()