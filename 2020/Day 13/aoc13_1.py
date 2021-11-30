file = open("aoc13_input.txt")
l = file.read().split("\n")
file.close()

m = int(l[0])
s = [int(j) for j in l[1].split(",") if j != "x"]
d = 0

while 1:
	for i in s:
		if (m+d) % i == 0:
			print(m, d, i, d*i)
			exit()
	d += 1