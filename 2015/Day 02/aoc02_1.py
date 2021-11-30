file = open("aoc02_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

s = 0

for i in l:
	a, b, c = [int(j) for j in i.split("x")]
	s += 2*a*b + 2*a*c + 2*b*c + min(a*b, a*c, b*c)

print(s)