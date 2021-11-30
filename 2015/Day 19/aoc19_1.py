file = open("aoc19_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

d = dict()

i = 0
while l[i]:
	s = l[i].split(" => ")
	if s[0] not in d.keys():
		d.setdefault(s[0], [])
	
	d[s[0]].append(s[1])
	i += 1

t = l[i+1]

p = 1
i = 0
while i < len(t):
	if t[i].isUpper():
		c = t[i]
		p *= len(c)-1
		i += d[c][0]

print(p)