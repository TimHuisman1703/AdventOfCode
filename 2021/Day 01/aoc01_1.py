file = open("aoc01_input.txt")
l = [int(j) for j in file.read().split("\n")]
file.close()

c = 0
for i in range(1, len(l)):
	if l[i-1] < l[i]:
		c += 1

print(c)