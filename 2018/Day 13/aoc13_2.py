file = open("aoc13_input.txt")
g = file.read().split("\n")
file.close()

pos = []
dir = []

for iy in range(len(g)):
	for ix in range(len(g[iy])):
		if g[iy][ix] == "^":
			pos.append((ix, iy))
			dir.append((0, -1))
			g[iy] = g[iy][:ix] + "|" + g[iy][ix+1:]
		elif g[iy][ix] == "v":
			pos.append((ix, iy))
			dir.append((0, 1))
			g[iy] = g[iy][:ix] + "|" + g[iy][ix+1:]
		elif g[iy][ix] == "<":
			pos.append((ix, iy))
			dir.append((-1, 0))
			g[iy] = g[iy][:ix] + "-" + g[iy][ix+1:]
		elif g[iy][ix] == ">":
			pos.append((ix, iy))
			dir.append((1, 0))
			g[iy] = g[iy][:ix] + "-" + g[iy][ix+1:]

state = [-1 for _ in range(len(pos))]

while 1:
	to_be_removed = set()

	for i in range(len(pos)):
		x, y = pos[i][0] + dir[i][0], pos[i][1] + dir[i][1]
		pos[i] = (x, y)
		
		if g[y][x] == "\\":
			dir[i] = (dir[i][1], dir[i][0])
		elif g[y][x] == "/":
			dir[i] = (-dir[i][1], -dir[i][0])
		elif g[y][x] == "+":
			if state[i] == -1:
				dir[i] = (dir[i][1], -dir[i][0])
			elif state[i] == 1:
				dir[i] = (-dir[i][1], dir[i][0])
			state[i] = (state[i] + 2) % 3 - 1
		
		for j in range(len(pos)):
			if i != j and pos[i] == pos[j]:
				to_be_removed.add(i)
				to_be_removed.add(j)
	
	for i in sorted(to_be_removed)[::-1]:
		state.pop(i)
		pos.pop(i)
		dir.pop(i)
	
	if len(pos) == 1:
		print(f"{pos[0][0]},{pos[0][1]}")
		break