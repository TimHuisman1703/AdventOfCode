file = open("aoc16_input.txt")
l = file.read()
file.close()

b = ""
for c in l:
	b += bin(int(c, 16))[2:].zfill(4)

i = 0
s = 0
while 1:
	if i > len(b) - 4:
		break

	version = int(b[i:i+3], 2)
	s += version
	type_id = int(b[i+3:i+6], 2)
	i += 6

	if type_id == 4:
		while b[i] == "1":
			i += 5
		i += 5
	else:
		i += 12 + 4 * (b[i] == "0")

print(s)