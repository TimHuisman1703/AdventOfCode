file = open("aoc03_input.txt")
l = file.read().split("\n")
file.close()

s = 0
for i in range(len(l)):
	s += int(l[i][(3*i)%len(l[i])] == "#")
print(s)