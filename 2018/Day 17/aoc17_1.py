file = open("aoc17_input.txt")
l = file.read().split("\n")
file.close()

# Yeah, that's big enough...
g = [[0 for _ in range(1000)] for _ in range(2000)]

min_y, max_y = 10**10, 0

for i in l:
	a, b = i.split(", ")
	x, a = a[0] == "x", int(a[2:])
	b, c = [int(j) for j in b[2:].split("..")]

	if x:
		for iy in range(b, c + 1):
			g[iy][a] = 3
		
		min_y = min(min_y, b)
		max_y = max(max_y, c)
	else:
		for ix in range(b, c + 1):
			g[a][ix] = 3
		
		min_y = min(min_y, a)
		max_y = max(max_y, a)

s = [(500, 0)]
c = 0

while s:
	x, y = s.pop()

	if g[y][x] >= 2:
		continue

	if y == max_y:
		c += 1
		g[y][x] = 1
		continue
	
	if g[y+1][x] >= 2:
		left_contained = right_contained = False

		left = x - 1
		while g[y + 1][left] >= 2:
			if g[y][left] == 3:
				left_contained = True
				left += 1
				break
			left -= 1
		
		right = x + 1
		while g[y + 1][right] >= 2:
			if g[y][right] == 3:
				right_contained = True
				right -= 1
				break
			right += 1
		
		for ix in range(left, right + 1):
			if g[y][ix] == 0:
				c += 1
			g[y][ix] = 1 + (left_contained and right_contained)
		
		if left_contained and right_contained:
			s.append((x, y - 1))
		
		if not left_contained:
			s.append((left, y + 1))
		if not right_contained:
			s.append((right, y + 1))
	else:
		if g[y][x] == 0:
			c += (y >= min_y)
			g[y][x] = 1
			s.append((x, y + 1))

print(c)