file = open("aoc11_input.txt")
l = file.read().split(",")
file.close()

x = y = 0
furthest = 0

for step in l:
	if step == "n":
		y += 1
	elif step == "s":
		y -= 1
	elif step == "nw":
		x -= 1
	elif step == "se":
		x += 1
	elif step == "ne":
		x += 1
		y += 1
	elif step == "sw":
		x -= 1
		y -= 1
	
	if x * y <= 0:
		furthest = max(furthest, abs(x) + abs(y))
	else:
		furthest = max(furthest, max(abs(x), abs(y)))

print(furthest)