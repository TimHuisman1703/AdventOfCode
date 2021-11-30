file = open("aoc20_input.txt")
l = file.read().split("\n")
file.close()

dim = 10

edges = {}

i = -1
while i < len(l)-1:
	i += 1
	tile_id = int(l[i].split()[1][:-1])
	
	i += 1
	normal = []
	for j in range(dim):
		normal.append(int(l[i].replace("#", "1").replace(".", "0"), 2))
		i += 1
	
	rotated = [0]*dim
	for j in range(dim):
		for k in range(len(normal)):
			rotated[j] += ((normal[k] >> (dim-1-j)) & 1) << (dim-1-k)
	
	edge = [normal[0], rotated[0], normal[-1], rotated[-1]]
	edge_flipped = []
	for j in edge:
		n = 0
		for k in range(dim):
			n += ((j >> k) & 1) << (dim - k - 1)
		edge_flipped.append(n)
	
	edges.setdefault(tile_id, edge + edge_flipped)

neighbors = {}

for i in edges.keys():
	neigh = set()
	for j in edges.keys():
		if i == j:
			continue
		for k in edges[i]:
			if k in edges[j]:
				neigh.add(j)
	neighbors.setdefault(i, neigh)

p = 1

for i in neighbors.keys():
	if len(neighbors[i]) == 2:
		p *= i

print(p)