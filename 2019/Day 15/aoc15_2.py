file = open("aoc15_input.txt")
l = [int(j) for j in file.read().split(",")]
file.close()

class IntCode:
	def __init__(self, code):
		self.code = {j: code[j] for j in range(len(code))}
		self.ip = 0
		self.input = []
		self.output = []
		self.base = 0
	
	def access(self, addr):
		try:
			return self.code[addr]
		except:
			return 0
	
	def parse_next(self, amount, writing=False):
		args = [0 for _ in range(amount)]
		for j in range(1, 1 + amount):
			mode = self.access(self.ip) // (10 ** (j + 1)) % 10

			if not (j == amount and writing):
				if mode == 0:
					args[j-1] = self.access(self.access(self.ip+j))
				elif mode == 1:
					args[j-1] = self.access(self.ip+j)
				elif mode == 2:
					args[j-1] = self.access(self.base + self.access(self.ip+j))
			else:
				if mode == 0:
					args[j-1] = self.access(self.ip+j)
				elif mode == 1:
					raise SyntaxError("tried to write to an immediate value")
				elif mode == 2:
					args[j-1] = self.base + self.access(self.ip+j)
		
		return args

	def execute(self):
		op = self.access(self.ip)

		# 1: 	Addition
		if op % 100 == 1:
			a, b, dst ,= self.parse_next(3, True)
			self.code[dst] = a + b
			self.ip += 4
			return None, ""
		
		# 2:	Multiplication
		if op % 100 == 2:
			a, b, dst ,= self.parse_next(3, True)
			self.code[dst] = a * b
			self.ip += 4
			return None, ""
		
		# 3:	Input
		if op % 100 == 3:
			dst ,= self.parse_next(1, True)
			if len(self.input) > 0:
				self.code[dst] = self.input.pop(0)
				self.ip += 2
				return None, ""
			else:
				return None, "no_input"
		
		# 4:	Output
		if op % 100 == 4:
			src ,= self.parse_next(1)
			self.output.append(src)
			self.ip += 2
			return self.output[-1], ""
		
		# 5:	Jump-If-True
		if op % 100 == 5:
			a, ind ,= self.parse_next(2)
			if a:
				self.ip = ind
			else:
				self.ip += 3
			return None, ""
		
		# 6:	Jump-If-False
		if op % 100 == 6:
			a, ind ,= self.parse_next(2)
			if not a:
				self.ip = ind
			else:
				self.ip += 3
			return None, ""
		
		# 7: 	Less Than
		if op % 100 == 7:
			a, b, dst ,= self.parse_next(3, True)
			self.code[dst] = int(a < b)
			self.ip += 4
			return None, ""
		
		# 8: 	Equals
		if op % 100 == 8:
			a, b, dst ,= self.parse_next(3, True)
			self.code[dst] = int(a == b)
			self.ip += 4
			return None, ""
		
		# 9: 	Adjust Relative Base
		if op % 100 == 9:
			a ,= self.parse_next(1)
			self.base += a
			self.ip += 2
			return None, ""
		
		if op % 100 == 99:	# 99:	Exit
			return None, "exit"
	
	def run(self, input=None):
		if input != None:
			self.input = input

		result = (None, "")
		while result[1] == "":
			result = self.execute()
		
		return self.output, result[1]
	
	def __repr__(self):
		string = str(self.code[0])
		i = 1
		while i in self.code.keys():
			string += "," + str(self.code[i])
			i += 1
		
		return string + f" [b = {self.base}]" + " < " + " < ".join(str(j) for j in self.input)

from collections import deque

intcode = IntCode(l)

x = y = 0
known = {(0, 0): 0}

dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def get_closest(known, x, y):
	q = deque([(x, y, "")])
	visited = set()

	while q:
		x, y, path = q.popleft()

		if (x, y) not in known:
			return path

		if (x, y) in visited:
			continue
		visited.add((x, y))
		
		for d in range(4):
			ix, iy = x + dir[d][0], y + dir[d][1]
			if (ix, iy) not in known or known[(ix, iy)] > 0:
				q.append((ix, iy, path + str(d)))
	
	return ""

while 1:
	instr = get_closest(known, x, y)

	if len(instr) == 0:
		break

	while len(instr) > 1:
		d, instr = int(instr[0]), instr[1:]
		key = (x + dir[d][0], y + dir[d][1])

		output, reason = intcode.run([d + 1])

		x += (d == 3) - (d == 2)
		y += (d == 1) - (d == 0)
	
	d = int(instr)
	intcode.output = []
	output, reason = intcode.run([d + 1])
	intcode.output = []
	
	key = (x + dir[d][0], y + dir[d][1])
	tile = output[0]
	known[key] = tile

	if tile > 0:
		x, y = key

	if tile == 2:
		sx, sy = x, y

q = deque([(0, sx, sy)])
visited = set()
m = 0

while q:
	cost, x, y = q.popleft()

	if (x, y) in visited:
		continue
	visited.add((x, y))
	
	if m < cost:
		m = cost

	for d in range(4):
		ix, iy = x + dir[d][0], y + dir[d][1]
		if known[(ix, iy)] > 0:
			q.append((cost + 1, ix, iy))

print(m)