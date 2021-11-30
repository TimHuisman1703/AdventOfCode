file = open("aoc02_input.txt")
l = [file.read().split("\n")
file.close()

x = y = 1
code = ""

for instr in l:
	for c in instr:
		if c == "L":
			if x > 0:
				x -= 1
		elif c == "R":
			if x < 2:
				x += 1
		elif c == "U":
			if y > 0:
				y -= 1
		elif c == "D":
			if y < 2:
				y += 1
	
	code += str(1 + x + 3*y)

print(code)