file = open("aoc03_input.txt")
l = file.read().split("\n")
file.close()

w = [l[j].split(",") for j in range(2)]

segments = []
x = y = 0
for instr in w[0]:
	d, strength = instr[0], int(instr[1:])
	nx = x + (int(d == "R") - int(d == "L")) * strength
	ny = y + (int(d == "D") - int(d == "U")) * strength
	
	if x == nx:
		segments.append((x, (min(y, ny), max(y, ny))))
	if y == ny:
		segments.append(((min(x, nx), max(x, nx)), y))

	x, y = nx, ny

possible = set()

x = y = 0
for instr in w[1]:
	d, strength = instr[0], int(instr[1:])
	nx = x + (int(d == "R") - int(d == "L")) * strength
	ny = y + (int(d == "D") - int(d == "U")) * strength

	if x == nx:
		cx, cy = x, (min(y, ny), max(y, ny))
		for sx, sy in segments:
			if type(sx) == int:
				if cx == sx and cy[0] <= sy[1] and sy[0] <= cy[1]:
					possible.add((cx, min(cy[0], sy[0])))
					possible.add((cx, max(cy[1], sy[1])))
			else:
				if sx[0] <= cx and cx <= sx[1] and cy[0] <= sy and sy <= cy[1]:
					possible.add((cx, sy))
	else:
		cx, cy = (min(x, nx), max(x, nx)), y
		for sx, sy in segments:
			if type(sx) == int:
				if cx[0] <= sx and sx <= cx[1] and sy[0] <= cy and cy <= sy[1]:
					possible.add((sx, cy))
			else:
				if cy == sy and cx[0] <= sx[1] and sx[0] <= cx[1]:
					possible.add((min(cx[0], sx[0]), cy))
					possible.add((max(cx[1], sx[1]), cy))

	x, y = nx, ny

dist = 1e100
for p in possible:
	curr = abs(p[0]) + abs(p[1])
	if curr == 0:
		continue

	if curr < dist:
		dist = curr

print(dist)