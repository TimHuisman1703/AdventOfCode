file = open("aoc14_input.txt")
l = file.read().split("\n")
file.close()

STEPS = 40

s = l[0]
letters = set([*s])

d = {}
for i in l[2:]:
	a, b = i.split(" -> ")
	d[a] = b
	letters.add(a[0])
	letters.add(a[1])
	letters.add(b)

mem = {}

def f(s, steps_left):
	global mem

	key = (s, steps_left)
	if key in mem.keys():
		return mem[key]

	if steps_left == 0:
		mem[key] = {k: s.count(k) for k in letters}
		return mem[key]

	mid = d[s]
	r1 = f(s[0] + mid, steps_left - 1)
	r2 = f(mid + s[1], steps_left - 1)

	r = {k: r1[k] + r2[k] for k in letters}
	r[mid] -= 1

	mem[key] = r
	return mem[key]

r = {k: 0 for k in letters}
for i in range(len(s) - 1):
	nr = f(s[i:i+2], STEPS)
	r = {k: r[k] + nr[k] for k in letters}

for k in s[1:len(s)-1]:
	r[k] -= 1

mi = min(r.values())
ma = max(r.values())

print(ma - mi)