file = open("aoc06_input.txt")
l = file.read().split("\n")
file.close()

occ = [[[0, chr(c)] for c in range(97, 123)] for j in range(len(l[0]))]

for message in l:
	for i in range(len(message)):
		c = message[i]
		index = ord(c)-97
		occ[i][index][0] += 1

result = ""
for i in range(len(l[0])):
	f = filter(lambda x: x[0] > 0, occ[i])
	c = sorted(f, key = lambda x: -x[0])[-1][1]
	result += c

print(result)