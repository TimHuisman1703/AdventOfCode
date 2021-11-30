file = open("aoc02_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

s = 0

for i in l:
	a, b, c = [int(j) for j in i.split("x")]
	d = sorted([a, b, c])
	s += 2*d[0] + 2*d[1] + a*b*c

print(s)