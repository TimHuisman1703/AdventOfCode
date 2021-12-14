file = open("aoc14_input.txt")
l = file.read().split("\n")
file.close()

STEPS = 10

s = l[0]
d = {}
for i in l[2:]:
	a, b = i.split(" -> ")
	d[a] = b

for _ in range(STEPS):
	ns = ""
	for i in range(len(s) - 1):
		ns += s[i] + d[s[i:i+2]]
	s = ns + s[-1]

mi = min([s.count(c) for c in set(s)])
ma = max([s.count(c) for c in set(s)])

print(ma - mi)