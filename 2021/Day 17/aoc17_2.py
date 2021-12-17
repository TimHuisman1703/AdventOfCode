file = open("aoc17_input.txt")
l = file.read().split()
file.close()

min_x, max_x = [int(j) for j in l[2][2:-1].split("..")]
min_y, max_y = [int(j) for j in l[3][2:].split("..")]

min_vx = 0
while min_vx * (min_vx + 1) // 2 < min_x:
	min_vx += 1
max_vx = max_x

min_vy = min_y
max_vy = -min_y

c = 0

for i in range(min_vy, max_vy + 1):
	for j in range(min_vx, max_vx + 1):
		vx, vy = j, i
		x, y = 0, 0
		while x <= max_x and y >= min_y:
			x += vx
			y += vy

			if vx < 0:
				vx += 1
			elif vx > 0:
				vx -= 1
			vy -= 1

			if min_x <= x and x <= max_x and min_y <= y and y <= max_y:
				c += 1
				break

print(c)