file = open("aoc25_input.txt")
code = file.read().split("\n")
file.close()

trial_length = 2**4

def parse(reg_or_imm):
	return reg[reg_or_imm] if reg_or_imm in "abcd" else int(reg_or_imm)

n = 1
while n < 1000000:
	out_count = 0
	ip = 0
	reg = {"a": n, "b": 0, "c": 0, "d": 0}

	while ip < len(code):
		args = code[ip].split()
		
		if args[0] == "inc":
			reg.update({args[1]: reg[args[1]] + 1})
			ip += 1
		elif args[0] == "dec":
			reg.update({args[1]: reg[args[1]] - 1})
			ip += 1
		elif args[0] == "cpy":
			if args[2] in "abcd":
				reg.update({args[2]: parse(args[1])})
			ip += 1
		elif args[0] == "jnz":
			if parse(args[1]) != 0:
				ip += int(parse(args[2]))
			else:
				ip += 1
		elif args[0] == "out":
			if out_count % 2 != parse(args[1]):
				if out_count >= trial_length:
					print("No, not it")
				break
			
			out_count += 1
			if out_count == trial_length:
				print(f"{n}?")
			ip += 1
	
	n += 1

	if n % 100 == 0:
		print(f"Nothing below {n}")