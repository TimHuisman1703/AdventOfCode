file = open("aoc08_input.txt")
s = file.read()
file.close()

WIDTH = 25
HEIGHT = 6

n = WIDTH * HEIGHT
l = [s[j:j+n] for j in range(0, len(s), n)]

img = [[None for ix in range(WIDTH)] for iy in range(HEIGHT)]

for iy in range(HEIGHT):
	for ix in range(WIDTH):
		i = 0
		while i < len(l):
			a = l[i][WIDTH * iy + ix]
			if a != "2":
				img[iy][ix] = "#" if a == "1" else " "
				break
			i += 1

print("\n".join("".join(row) for row in img))