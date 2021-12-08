file = open("aoc08_input.txt")
l = file.read().split("\n")
file.close()

c = 0

for i in l:
	m = {}
	s, d = i.split(" | ")
	s = s.split()
	d = d.split()

	for j in s:
		if len(j) == 2:
			m[1] = set(list(j))
		if len(j) == 4:
			m[4] = set(list(j))
		if len(j) == 3:
			m[7] = set(list(j))
		if len(j) == 7:
			m[8] = set(list(j))
	
	for j in s:
		a = set(list(j))
		if a in m.values():
			continue

		if len(a) == 6 and len(a - m[4]) == 2:
			m[9] = a
		if len(a) == 5 and len(a - m[1]) == 3:
			m[3] = a
	
	mid = list((m[3] & m[4]) - m[1])[0]

	for j in s:
		a = set(list(j))
		if a in m.values():
			continue

		if len(a) == 6 and mid not in a:
			m[0] = a
	
	for j in s:
		a = set(list(j))
		if a in m.values():
			continue

		if len(a) == 6:
			m[6] = a
	
	for j in s:
		a = set(list(j))
		if a in m.values():
			continue
		
		if len(m[6] - a) == 1:
			m[5] = a
		else:
			m[2] = a

	curr = 0
	for j in d:
		a = set(list(j))
		for k in range(10):
			if m[k] == a:
				curr = curr * 10 + k

	c += curr

print(c)