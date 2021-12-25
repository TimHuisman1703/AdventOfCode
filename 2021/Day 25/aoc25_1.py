file = open("aoc25_input.txt")
l = file.read().split("\n")
file.close()

h, w = len(l), len(l[0])

e = set()
s = set()
for iy in range(h):
	for ix in range(w):
		if l[iy][ix] == ">":
			e.add((ix, iy))
		elif l[iy][ix] == "v":
			s.add((ix, iy))

steps = 0
moved = True
while moved:
	steps += 1
	moved = False
	
	ne = set(e)
	ns = set(s)
	for p in e:
		q = ((p[0] + 1) % w, p[1])
		if not q in e and not q in s:
			moved = True
			ne.add(q)
			ne.remove(p)
	for p in s:
		q = (p[0], (p[1] + 1) % h)
		if not q in ne and not q in s:
			moved = True
			ns.add(q)
			ns.remove(p)
	
	e = ne
	s = ns

print(steps)