file = open("aoc07_input.txt")
l = file.read().split("\n")
file.close()

s = set()
p = -1
while len(s) > p:
	p = len(s)
	for i in l:
		if "shiny gold" in i[10:]:
			s.add(' '.join(i.split()[0:2]))
		t = set()
		for j in s:
			if j in i[10:]:
				t.add(' '.join(i.split()[0:2]))
		s = s | t

print(s)
print(len(s))