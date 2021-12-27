file = open("aoc20_input.txt")
l = file.read().split("\n")
file.close()

import heapq

g = [[0 for _ in range(len(l[0]))] for _ in range(len(l))]
portals = []

for iy in range(len(l)):
	for ix in range(len(l[0])):
		if l[iy][ix] == ".":
			if l[iy-1][ix].isalpha():
				portals.append((l[iy-2][ix] + l[iy-1][ix], (ix, iy)))
			elif l[iy+1][ix].isalpha():
				portals.append((l[iy+1][ix] + l[iy+2][ix], (ix, iy)))
			elif l[iy][ix-1].isalpha():
				portals.append((l[iy][ix-2] + l[iy][ix-1], (ix, iy)))
			elif l[iy][ix+1].isalpha():
				portals.append((l[iy][ix+1] + l[iy][ix+2], (ix, iy)))
		else:
			g[iy][ix] = 1

tele = {}
for i in range(len(portals)):
	if portals[i][0] == "AA":
		x, y = portals[i][1]
	elif portals[i][0] == "ZZ":
		dx, dy = portals[i][1]
	else:
		for j in range(i + 1, len(portals)):
			if portals[i][0] == portals[j][0]:
				tele[portals[i][1]] = portals[j][1]
				tele[portals[j][1]] = portals[i][1]

q = [(0, x, y, 0)]
visited = set()

while q:
	cost, x, y, level = heapq.heappop(q)

	if (x, y, level) in visited:
		continue
	visited.add((x, y, level))

	if x == dx and y == dy and level == 0:
		print(cost)
		break
	
	if (x, y) in tele.keys():
		ix, iy = tele[(x, y)]
		going_in = 3 <= x < len(g[0]) - 3 and 3 <= y < len(g) - 3
		if level > 0 or going_in:
			heapq.heappush(q, (cost + 1, ix, iy, level - 1 + 2 * going_in))
	
	for ix, iy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
		if g[iy][ix] == 0:
			heapq.heappush(q, (cost + 1, ix, iy, level))