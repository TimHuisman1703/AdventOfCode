file = open("aoc10_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

t = l[0]

for i in range(50):
	r = ""
	c = 1
	n = t[0]
	for j in range(1, len(t)):
		if t[j] == t[j-1]:
			c += 1
		else:
			r += str(c)+t[j-1]
			n = t[j]
			c = 1
	r += str(c)+t[-1]

	t = r

print(len(t))