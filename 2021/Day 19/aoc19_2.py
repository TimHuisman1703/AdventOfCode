file = open("aoc19_input.txt")
l = file.read().split("\n\n")
file.close()

THRESHOLD = 12

b = []
for s in l:
	p = set()
	for c in s.split("\n")[1:]:
		x, y, z = [int(j) for j in c.split(",")]
		p.add((x, y, z))
	b.append(p)

rotations = [
	(0, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0),
	(0, 1, 0), (1, 1, 0), (2, 1, 0), (3, 1, 0),
	(0, 2, 0), (1, 2, 0), (2, 2, 0), (3, 2, 0),
	(0, 3, 0), (1, 3, 0), (2, 3, 0), (3, 3, 0),
	(0, 0, 1), (1, 0, 1), (2, 0, 1), (3, 0, 1),
	(0, 0, 3), (1, 0, 3), (2, 0, 3), (3, 0, 3)
]

connections = []
for i in range(len(b) - 1):
	print(f"i = {i}")
	for j in range(i + 1, len(b)):
		acc = {}
		
		for p in b[i]:
			for q in b[j]:
				transformations = []
				for r in rotations:
					x, y, z = q
					for _ in range(r[2]):
						y, z = -z, y
					for _ in range(r[1]):
						x, z = -z, x
					for _ in range(r[0]):
						x, y = y, -x
					transformations.append((r, p[0] - x, p[1] - y, p[2] - z))
				
				for t in transformations:
					if t not in acc.keys():
						acc[t] = 0
					acc[t] += 1
		
		best = max(acc, key=lambda x:acc[x])

		if acc[best] >= THRESHOLD:
			connections.append((i, j, best + (True,)))
			connections.append((j, i, best + (False,)))

tree = set([0])
transformations = [[] for _ in range(len(b))]
while len(tree) < len(b):
	for c in connections:
		if c[0] in tree and c[1] not in tree:
			i = c[0]
			j = c[1]
			t = c[2]
			transformations[j] = [t] + transformations[i]
			tree.add(j)

pos = []
for j in range(len(b)):
	x = y = z = 0
	
	for t in transformations[j]:
		r, dx, dy, dz, forward = t
		if forward:
			for _ in range(r[2]):
				y, z = -z, y
			for _ in range(r[1]):
				x, z = -z, x
			for _ in range(r[0]):
				x, y = y, -x
		
			x += dx
			y += dy
			z += dz
		else:
			x -= dx
			y -= dy
			z -= dz

			for _ in range(r[0]):
				x, y = -y, x
			for _ in range(r[1]):
				x, z = z, -x
			for _ in range(r[2]):
				y, z = z, -y
	
	pos.append((x, y, z))

m = 0
for i in range(len(b) - 1):
	for j in range(i + 1, len(b)):
		m = max(abs(pos[i][0] - pos[j][0]) + abs(pos[i][1] - pos[j][1]) + abs(pos[i][2] - pos[j][2]), m)

print(m)