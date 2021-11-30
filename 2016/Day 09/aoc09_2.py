file = open("aoc09_input.txt")
s = file.read()
file.close()

def calc_length(s):
	c = 0
	i = 0

	while i < len(s):
		if s[i] != "(":
			c += 1
			i += 1
		else:
			start = i+1
			while s[i] != ")":
				i += 1
			end = i

			length, rep = [int(j) for j in s[start:end].split("x")]
			i += 1
			
			c += rep*calc_length(s[end+1:end+length+1])
			i += length
	
	return c

print(calc_length(s))