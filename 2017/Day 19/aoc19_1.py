file = open("aoc19_input.txt")
g = file.read().split("\n")
file.close()

dir = (0, 1)
x, y = g[0].find("|"), 0

path = ""

while True:
	dx, dy = dir
	x, y = x + dx, y + dy
	
	c = g[y][x]
	if c == "+":
		if dir[0] == 0:
			if g[y][x+1] in " |":
				dir = (-1, 0)
			else:
				dir = (1, 0)
		else:
			if g[y+1][x] in " -":
				dir = (0, -1)
			else:
				dir = (0, 1)
	elif c == " ":
		break
	elif c not in "-|":
		path += c

print(path)