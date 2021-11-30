file = open("aoc16_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

a = []

for i in l:
	d = dict()
	s = (i+",").split()
	for j in range(2, 8, 2):
		d.setdefault(s[j][:-1], int(s[j+1][:-1]))
	a.append(d)

s = set(range(len(l)))

req = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

for i in req.keys():
	ns = set(j for j in s)
	for j in s:
		try:
			if a[j][i] != req[i]:
				ns.remove(j)
		except:
			pass
	s = ns

print(s)
print(f"Sue {[*s][0]+1}")