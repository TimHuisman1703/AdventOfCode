file = open("aoc02_input.txt")
code = [int(j) for j in file.read().split(",")]
file.close()

OUTPUT = 19690720

backup = code[:]

for a in range(100):
	for b in range(100):
		ip = 0

		code = backup[:]
		code[1] = a
		code[2] = b

		while ip < len(code):
			if code[ip] == 1:
				args = code[ip+1:ip+4]
				code[args[2]] = code[args[0]] + code[args[1]]
				ip += 4
				continue
			
			if code[ip] == 2:
				args = code[ip+1:ip+4]
				code[args[2]] = code[args[0]] * code[args[1]]
				ip += 4
				continue
			
			if code[ip] == 99:
				break
		
		if code[0] == OUTPUT:
			print(100 * a + b)