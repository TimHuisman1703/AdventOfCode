file = open("aoc16_input.txt")
l = file.read().split("\n")
file.close()

r = []
names = []

i = 0
while l[i] != "":
	name, p = l[i].split(": ")
	names.append(name)
	rp = []
	for j in p.split(" or "):
		n = j.split("-")
		rp.append(int(n[0]))
		rp.append(int(n[1]))
	r.append(rp)
	i += 1

a = i
v = []
# available = list(range(a))

i += 5
s = i

while i < len(l):
	p = [int(j) for j in l[i].split(",")]
	valid = True
	for j in range(a):
		in_range = False
		for k in r:
			for m in range(0, len(k), 2):
				if p[j] in range(k[m], k[m+1]+1):
					in_range = True
		if not in_range:
			valid = False
	if valid:
		v.append(p)
	i += 1

g = [[1 for j in range(a)] for i in range(a)]

available_attr = list(range(a))
available_nr = list(range(a))

while sum(sum(j for j in i) for i in g) > a:
	for attr in range(a): # The attribute (with name) for which we're going to test stuff
		for nr in range(a): # The value number for which
			for inst in v: # A particular instance list
				in_range = False
				for i in range(0, len(r[attr]), 2): # Index of range values
					if inst[nr] in range(r[attr][i], r[attr][i+1]+1):
						in_range = True
				if not in_range:
					g[attr][nr] = 0
	
	# Vertical Elimination
	for i in range(a):
		if sum(g[i]) == 1:
			index = g[i].index(1)
			for j in range(a):
				g[j][index] = int(i == j)
print("\n".join(" ".join(str(j) for j in i) for i in g))

own = [int(j) for j in l[s-3].split(",")]

p = 1
for i in range(a):
	if "departure" in names[i]:
		for j in range(a):
			if g[i][j]:
				p *= own[j]
print(p)