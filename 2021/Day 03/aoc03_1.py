file = open("aoc03_input.txt")
l = file.read().split("\n")
file.close()

g = ""
e = ""
for i in range(len(l[0])):
	ones = 0
	zeros = 0
	for j in l:
		if j[i] == "0":
			zeros += 1
		else:
			ones += 1

	if ones >= zeros:
		g += "1"
		e += "0"
	else:
		g += "0"
		e += "1"

print(int(g, 2) * int(e, 2))