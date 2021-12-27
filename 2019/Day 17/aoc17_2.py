file = open("aoc17_input.txt")
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
	
	def run(self, input=None, clear=True):
		if input != None:
			self.input = input

		result = (None, "")
		while result[1] == "":
			result = self.execute()
		
		output = self.output
		if clear:
			self.output = []
		return output, result[1]
	
	def __repr__(self):
		string = str(self.code[0])
		i = 1
		while i in self.code.keys():
			string += "," + str(self.code[i])
			i += 1
		
		return string + f" [b = {self.base}]" + " < " + " < ".join(str(j) for j in self.input)

l[0] = 2

intcode = IntCode(l)
output, reason = intcode.run()

g = [j for j in "".join(chr(j) for j in output).split("\n") if j]

m = [ord(j) for j in "A,B,B,A,C,A,C,A,C,B\n"]
a = [ord(j) for j in "L,6,R,12,R,8\n"]
b = [ord(j) for j in "R,8,R,12,L,12\n"]
c = [ord(j) for j in "R,12,L,12,L,4,L,4\n"]
v = [ord(j) for j in "n\n"]

output, reason = intcode.run(m + a + b + c + v)

print(output[-1])

# Done manually, cause I'm not programming this...
# ..............CCCCC................................
# ..............C...C................................
# ....AAAAAAAAAA#AA.C................................
# ....A.........C.A.C................................
# CCCC#CCCCCCCC.CA#A#AA..............................
# C...A.......C...A.C.A..............................
# C...A.......C...A.C.A.....................AAAAAAAAA
# C...A.......C...A.C.A.....................A.......B
# CCCCC.......C...A.C.A.....................A.......B
# ............C...A.C.A.....................A.......B
# ....CCCCCCCC#CCCA.C.A.....................A.......B
# ....C.......C.....C.A.....................A.......B
# ....C.ACCCCC#CCCCCC.A.....................A.......B
# ....C.A.....C.......A.....................A.......B
# ....C.A.....C.....BB#BBBBBBBBBB.......BBBB#BBBBBBBB
# ....C.A.....C.....A.A.........B.......B...A........
# ....C.A.....AAAAAA#AA.........B.......B...A........
# ....C.A...........A...........B.......B...A........
# ....C.A.CBBBBBBBB.A...........B.......B...AAAAAA^..
# ....C.A.C.......B.A...........B.......B............
# ....C.AA#AAAAAAA#AA...........B.......B............
# ....C...C.......B.............B.......B............
# ....CCCCC.......B.............B.......B............
# ................B.............B.......B............
# ................B.............B.......B............
# ................B.............B.......B............
# ................B.............BBBBBBBBB............
# ................B..................................
# ................B..................................
# ................B..................................
# ................BBBBBBBBBBBBB......................