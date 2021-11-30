file = open("aoc23_input.txt")
code = file.read().split("\n")
file.close()

def parse(x):
	try:
		return int(x)
	except:
		return reg[x]

reg = {name: int(name == "a") for name in "abcdefgh"}
ip = 0

c = 0

while ip < len(code):
	print(ip+1, code[ip], "\t", reg)
	command, *args = code[ip].split()

	if command == "set":
		reg.update({args[0]: parse(args[1])})
	elif command == "sub":
		reg.update({args[0]: reg[args[0]] - parse(args[1])})
	elif command == "mul":
		reg.update({args[0]: reg[args[0]] * parse(args[1])})
		c += 1
	elif command == "jnz":
		if parse(args[0]) != 0:
			ip += parse(args[1])
			continue
	
	ip += 1

print(reg["h"])