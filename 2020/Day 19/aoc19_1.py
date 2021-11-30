file = open("aoc19_input.txt")
l = file.read().split("\n")
file.close()

def cartesian_concat(a, b):
	r = []
	for i in a:
		for j in b:
			r.append(i+j)
	return r

def get_possibilities(n):
	if isinstance(d[n][0], list):
		sl = []
		for i in range(len(d[n])):
			slcp = [""]
			for j in range(len(d[n][i])):
				slcp = cartesian_concat(slcp, get_possibilities(d[n][i][j]))
			sl += slcp
		d.update({n: sl})
	return d[n]

d = {}

for i in range(len(l)):
	if l[i] == "":
		break
	nr = int(l[i].split(":")[0])
	if "\"" in l[i]:
		d.setdefault(nr, [l[i].split("\"")[1]])
	else:
		s = l[i][l[i].index(" ")+1:].split(" | ")
		n = []
		for j in s:
			n.append(list(map(int, j.split())))
		d.setdefault(nr, n)

i += 1

w = set()
while i < len(l):
	w.add(l[i])
	i += 1

p = get_possibilities(0)
print(len(set(p) & w))