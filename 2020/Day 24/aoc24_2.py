file = open("aoc24_input.txt")
l = file.read().split("\n")
file.close()

def check_surroundings(d, x, y):
	c = 0
	for dy in range(-1, 2):
		for dx in range(-1+int(dy > 0), 2-int(dy < 0), 1+int(dy == 0)):
			try:
				c += d[str(x+dx)+","+str(y+dy)]
			except:
				pass
	return c

d = {}

for i in l:
	x = y = 0
	j = 0
	while j < len(i):
		if i[j] == "w":
			x -= 1
		elif i[j] == "e":
			x += 1
		elif i[j] == "n":
			y -= 1
			j += 1
			if i[j] == "w":
				x -= 1
		else:
			y += 1
			j += 1
			if i[j] == "e":
				x += 1
		j += 1
	
	try:
		d.pop(str(x)+","+str(y))
	except:
		d.setdefault(str(x)+","+str(y), 1)

days = 100

for day in range(days):
	nd = dict()

	for i in d.keys():
		x, y = [int(j) for j in i.split(",")]
		c = 0
		for dy in range(-1, 2):
			for dx in range(-1+int(dy > 0), 2-int(dy < 0), 1+int(dy == 0)):
				key = str(x+dx)+","+str(y+dy)
				c = check_surroundings(d, x+dx, y+dy)
				try:
					lmao_doesnt_matter = d[key]
					if 0 < c < 3:
						nd.setdefault(key, 1)
				except:
					if c == 2:
						nd.setdefault(key, 1)
	d = nd
	print(f"Day {day+1}: {len(d.keys())}")