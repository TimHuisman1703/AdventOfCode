file = open("aoc06_input.txt")
l = file.read().split("\n")
file.close()

THRESHOLD = 10000

points = [tuple([int(k) for k in j.split(", ")]) for j in l]

avg_x = sum(j[0] for j in points) // len(points)
hori_dist = [sum(abs(avg_x - j[0]) for j in points)]

ix = avg_x
while 1:
	ix += 1
	
	dist = sum(abs(ix - j[0]) for j in points)
	if dist < THRESHOLD:
		hori_dist.append(dist)
	else:
		break

ix = avg_x
while 1:
	ix -= 1
	
	dist = sum(abs(ix - j[0]) for j in points)
	if dist < THRESHOLD:
		hori_dist.append(dist)
	else:
		break

avg_y = sum(j[1] for j in points) // len(points)
vert_dist = [sum(abs(avg_y - j[1]) for j in points)]

iy = avg_y
while 1:
	iy += 1
	
	dist = sum(abs(iy - j[1]) for j in points)
	if dist < THRESHOLD:
		vert_dist.append(dist)
	else:
		break

iy = avg_y
while 1:
	iy -= 1
	
	dist = sum(abs(iy - j[1]) for j in points)
	if dist < THRESHOLD:
		vert_dist.append(dist)
	else:
		break

print(hori_dist)
print(vert_dist)

area_size = 0
for dy in vert_dist:
	for dx in hori_dist:
		if dy + dx < THRESHOLD:
			area_size += 1

print(area_size)