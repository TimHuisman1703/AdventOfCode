file = open("aoc01_input.txt")
l = [int(j) for j in file.read().split("\n")]
file.close()

s = 0
for i in l:
	c = i
	while c > 0:
		c = c // 3 - 2

		if c > 0:
			s += c

print(s)