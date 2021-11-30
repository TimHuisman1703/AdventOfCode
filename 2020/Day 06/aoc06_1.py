file = open("aoc06_input.txt")
l = file.read().split("\n")
file.close()

s = 0
c = [0]*26
for i in range(len(l)+1):
	if i == len(l) or l[i] == "":
		s += sum(c)
		print(c)
		c = [0]*26
	else:
		for j in l[i]:
			c[ord(j)-97] = 1

print(s)