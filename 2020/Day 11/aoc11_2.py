file = open("aoc11_input.txt")
l = [[int(j == "L") for j in i] for i in file.read().split("\n")]
file.close()

import copy

def get_occupied_neighbors(l, x, y):
	c = 0
	for dy in range(-1, 2):
		for dx in range(-1, 2):
			if dx == dy == 0:
				continue
			ix = x+dx
			iy = y+dy
			while -1 < ix < len(l[0]) and -1 < iy < len(l):
				if l[iy][ix] > 0:
					c += l[iy][ix]-1
					break
				ix += dx
				iy += dy
	
	return c

def print_seats(l):
	print("---")
	seats = ".L#"
	for i in l:
		print(''.join(seats[j] for j in i))

changes = 1
while changes:
	print_seats(l)
	changes = 0
	n = copy.deepcopy(l)
	for iy in range(len(l)):
		for ix in range(len(l[0])):
			p = get_occupied_neighbors(l, ix, iy)
			if p >= 5 and l[iy][ix] == 2:
				n[iy][ix] = 1
				changes += 1
			if p == 0 and l[iy][ix] == 1:
				n[iy][ix] = 2
				changes += 1
	l = n

print(sum(i.count(2) for i in l))