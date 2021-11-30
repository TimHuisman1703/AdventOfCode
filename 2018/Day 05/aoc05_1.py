file = open("aoc05_input.txt")
s = file.read()
file.close()

i = 0
while i < len(s)-1:
	c = sorted(s[i:i+2])
	
	if c[0].isupper() and c[1].islower() and c[0].lower() == c[1]:
		s = s[:i] + s[i+2:]
		i -= int(i > 0)
	else:
		i += 1

print(len(s))