file = open("aoc08_input.txt")
l = file.read().split("\n")
file.close()

c = 0
for i in l:
	s, d = i.split(" | ")
	s = s.split()
	d = d.split()

	for i in d:
		if len(i) in [2, 3, 4, 7]:
			c += 1

print(c)