file = open("aoc03_input.txt")
l = file.read().split("\n")
file.close()

r = [1, 3, 5, 7, 1]
d = [1, 1, 1, 1, 2]

s = [0]*5
for i in range(5):
	for j in range(0, len(l), d[i]):
		s[i] += int(l[j][(r[i]*(j//d[i]))%len(l[j])] == "#")
	print(s)

print(s[0]*s[1]*s[2]*s[3]*s[4])