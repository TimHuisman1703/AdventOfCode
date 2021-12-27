file = open("aoc07_input.txt")
l = [int(j) for j in file.read().split(",")]
file.close()

class IntCode:
	def __init__(self, code):
		self.code = code[:]
		self.ip = 0
		self.input = []
		self.output = []
	
	def parse_next(self, amount, writing=False):
		return [self.code[self.ip+j] if self.code[self.ip] // (10 ** (j + 1)) % 10 == 1 or (j == amount and writing) else self.code[self.code[self.ip+j]] for j in range(1, 1 + amount)]

	def execute(self):
		op = self.code[self.ip]

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
			if self.input:
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
		
		if op % 100 == 99:	# 99:	Exit
			return None, "exit"
	
	def __repr__(self):
		return ",".join(f"{self.code[j]}" if j != self.ip else f"({self.code[j]})" for j in range(len(self.code))) \
			+ " < " + " < ".join(str(j) for j in self.input)

from itertools import permutations

best = 0

for order in permutations(range(5)):
	signal = 0

	for i in range(5):
		intcode = IntCode(l)
		intcode.input = [order[i], signal]

		result = (None, "")
		while result[0] == None:
			result = intcode.execute()
		
		signal = result[0]
	
	best = max(best, signal)

print(best)