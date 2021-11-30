file = open("aoc05_input.txt")
l = file.read().replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1").split("\n")
file.close()

m = 0

for i in l:
	if int(i, 2) > m:
		m = int(i, 2)

print(m)