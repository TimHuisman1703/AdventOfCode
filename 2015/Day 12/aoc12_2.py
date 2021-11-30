file = open("aoc12_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

def find_next_close(i):
	c = 1
	while c > 0:
		if t[i] == "{":
			c += 1
		elif t[i] == "}":
			c -= 1
		i += 1
	return i

t = l[0]
map_stack = [0]

i = 0
while i < len(t):
	print(t[i-100:i], map_stack)
	if t[i] == "-" or t[i].isdigit():
		e = i+1
		while t[e].isdigit():
			e += 1
		map_stack[-1] += int(t[i:e])
		i = e-1
	elif t[i] == "{":
		map_stack += [0]
	elif t[i] == "}":
		map_stack[-2] += map_stack[-1]
		map_stack = map_stack[:-1]
	elif t[i:i+6] == ":\"red\"":
		map_stack = map_stack[:-1]
		i = find_next_close(i)-1
	i += 1

print(map_stack[0])