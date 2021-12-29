file = open("aoc23_input.txt")
l = file.read().split("\n")
file.close()

class Diamond:
	def __init__(self, a, A, b, B, c, C, d, D, power):
		self.a = a
		self.A = A
		self.b = b
		self.B = B
		self.c = c
		self.C = C
		self.d = d
		self.D = D
		self.power = power
	
	@classmethod
	def from_radius(cls, x, y, z, r):
		return cls(
			x + y + z - r,
			x + y + z + r + 1,
			x + y - z - r,
			x + y - z + r + 1,
			x - y + z - r,
			x - y + z + r + 1,
			x - y - z - r,
			x - y - z + r + 1,
			1
		)

	def segment(x, y):
		global maximum

		if (x.A <= y.a or y.A <= x.a) \
			or (x.B <= y.b or y.B <= x.b) \
			or (x.C <= y.c or y.C <= x.c) \
			or (x.D <= y.d or y.D <= x.d):
			return [x], []
		
		exc = []
		
		if x.a < y.a:
			exc.append(Diamond(x.a, y.a, x.b, x.B, x.c, x.C, x.d, x.D, x.power))
		if y.A < x.A:
			exc.append(Diamond(y.A, x.A, x.b, x.B, x.c, x.C, x.d, x.D, x.power))
		
		a = x.a if x.a >= y.a else y.a
		A = x.A if x.A <= y.A else y.A

		if x.b < y.b:
			exc.append(Diamond(a, A, x.b, y.b, x.c, x.C, x.d, x.D, x.power))
		if y.B < x.B:
			exc.append(Diamond(a, A, y.B, x.B, x.c, x.C, x.d, x.D, x.power))
		
		b = x.b if x.b >= y.b else y.b
		B = x.B if x.B <= y.B else y.B

		if x.c < y.c:
			exc.append(Diamond(a, A, b, B, x.c, y.c, x.d, x.D, x.power))
		if y.C < x.C:
			exc.append(Diamond(a, A, b, B, y.C, x.C, x.d, x.D, x.power))
		
		c = x.c if x.c >= y.c else y.c
		C = x.C if x.C <= y.C else y.C

		if x.c < y.c:
			exc.append(Diamond(a, A, b, B, c, C, x.d, y.d, x.power))
		if y.C < x.C:
			exc.append(Diamond(a, A, b, B, c, C, y.D, x.D, x.power))
		
		d = x.d if x.d >= y.d else y.d
		D = x.D if x.D <= y.D else y.D

		inc = Diamond(a, A, b, B, c, C, d, D, x.power + 1)
		maximum = maximum if maximum >= x.power + 1 else x.power + 1

		return exc, inc
	
	def dist_to_origin(self):
		dist = 0

		dist = max(dist, self.a, -self.A)
		dist = max(dist, self.b, -self.B)
		dist = max(dist, self.c, -self.C)
		dist = max(dist, self.d, -self.D)

		return dist
	
	def __repr__(self):
		return f"({self.power}): " \
			+ f"{self.a} <= x + y + z < {self.A}, " \
			+ f"{self.b} <= x + y - z < {self.B}, " \
			+ f"{self.c} <= x - y + z < {self.C}, " \
			+ f"{self.d} <= x - y - z < {self.D}"

DIFF = 1

diamonds = []
maximum = 0

for i in range(len(l)):
	info = l[i]

	pos, r = info.split()
	x, y, z, _ = pos.split(",")
	x, y, z = int(x[5:]), int(y), int(z[:-1])
	r = int(r[2:])
	n = Diamond.from_radius(x, y, z, r)

	excluded = []
	included = []
	for d in diamonds:
		exc, inc = d.segment(n)
		excluded.extend(exc)
		if inc:
			included.append(inc)
	
	added = [n]
	for d in included:
		new_added = []
		for n in added:
			_, inc = n.segment(d)
			if inc:
				new_added.append(inc)
		added = new_added
	
	diamonds = [j for j in excluded + included + added if maximum - j.power <= DIFF]

dist = 10**100
for d in diamonds:
	if d.power == maximum:
		dist = min(dist, d.dist_to_origin())

print(dist)