file = open("aoc02_input.txt")
l = file.read().split("\n")
file.close()

keypad = [
	"  1  ",
	" 234 ",
	"56789",
	" ABC ",
	"  D  ",
]

x, y = 0, 2
code = ""

for instr in l:
	for c in instr:
		if c == "L":
			if x > abs(y-2):
				x -= 1
		elif c == "R":
			if x < 4 - abs(y-2):
				x += 1
		elif c == "U":
			if y > abs(x-2):
				y -= 1
		elif c == "D":
			if y < 4 - abs(x-2):
				y += 1
	
	code += keypad[y][x]

print(code)