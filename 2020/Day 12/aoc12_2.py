file = open("aoc12_input.txt")
l = file.read().split("\n")
file.close()

print(l)

wx = 10
wy = -1
x = y = 0

for i in l:
	n = int(i[1:])

	if i[0] == "N":
		wy -= n
	elif i[0] == "S":
		wy += n
	elif i[0] == "W":
		wx -= n
	elif i[0] == "E":
		wx += n
	elif i[0] == "L":
		for _ in range(n//90):
			wx, wy = wy, -wx
	elif i[0] == "R":
		for _ in range(n//90):
			wx, wy = -wy, wx
	elif i[0] == "F":
		x += wx*n
		y += wy*n
	
	print(x, y, wx, wy)
print(abs(x) + abs(y))