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
				print(f"{pos[i][0]},{pos[i][1]}")
				exit()