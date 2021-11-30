file = open("aoc02_input.txt")
l = file.read().split("\n")
file.close()

s = 0
t = 0
for i in l:
	t += 1
	d = i.split()
	pos1, pos2 = [int(j)-1 for j in d[0].split("-")]
	c = d[1][0]
	if((d[2][pos1] == c) != (d[2][pos2] == c)):
		s += 1
		print(i)
print(s, t)