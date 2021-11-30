file = open("aoc16_input.txt")
l = file.read().split("\n")
file.close()

r = []

i = 0
while l[i] != "":
	p = l[i].split(": ")[1]
	for j in p.split(" or "):
		n = j.split("-")
		r.append(int(n[0]))
		r.append(int(n[1]))
	i += 1

a = i
s = 0

i += 5
while i < len(l):
	p = [int(j) for j in l[i].split(",")]
	for j in range(a):
		in_range = False
		for k in range(0, len(r), 2):
			if p[j] in range(r[k], r[k+1]+1):
				in_range = True
		if not in_range:
			print(i, j, p[j], r[j])
			s += p[j]
	i += 1
print(s)