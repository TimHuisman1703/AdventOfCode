file = open("aoc14_input.txt")
l = file.read().split("\n")
file.close()

d = {}
references = {"ORE": 1}

for i in l:
	a, b = i.split(" => ")

	r = set()
	for j in a.split(", "):
		c, m = j.split()
		r.add((int(c), m))

		if m not in references.keys():
			references[m] = 0
		references[m] += 1
	
	c, m = b.split()
	d[m] = (int(c), r)

	if m not in references.keys():
		references[m] = 0
	references[m] += 1

backup = references.copy()

def is_trillion_enough(fuel):
	references = backup.copy()
	needed = {key: fuel * int(key == "FUEL") for key in references.keys()}

	while references:
		m = sorted(references, key=lambda x: references[x])[0]
		references.pop(m)
		
		if m == "ORE":
			return needed[m] <= 1000000000000
		
		c, r = d[m]
		n = (needed[m] - 1) // c + 1

		for c, i in r:
			references[i] -= 1
			needed[i] += c * n

max_fuel = 1
while is_trillion_enough(max_fuel):
	max_fuel *= 2

min_fuel = max_fuel // 2
while min_fuel < max_fuel:
	mid = (min_fuel + max_fuel + 1) // 2
	
	if not is_trillion_enough(mid):
		max_fuel = mid - 1
	else:
		min_fuel = mid

print(min_fuel)