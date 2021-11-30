file = open("aoc23_input.txt")
code = file.read().split("\n")
file.close()

import time

ip = 0
reg = {"a": 12, "b": 0, "c": 0, "d": 0}

toggle_op_codes = {
	"inc": "dec",
	"dec": "inc",
	"tgl": "inc",
	"jnz": "cpy",
	"cpy": "jnz"
}

def parse(reg_or_imm):
	return reg[reg_or_imm] if reg_or_imm in "abcd" else int(reg_or_imm)

while ip < len(code):
	args = code[ip].split()

	# Quick calculations line 5-10
	if ip == 4:
		if code[4:10] == [
			"cpy b c",
			"inc a",
			"dec c",
			"jnz c -2",
			"dec d",
			"jnz d -5"]:
			result = reg["a"] + reg["b"] * reg["d"]
			reg = {"a": result, "b": reg["b"], "c": 0, "d": 0}
			ip = 10
			continue
	
	# Quick calculations line 14-16
	if ip == 13:
		if code[13:16] == [
			"dec d",
			"inc c",
			"jnz d -2"]:
			result = reg["c"] + reg["d"]
			reg.update({"c": result})
			reg.update({"d": 0})
			ip = 16
			continue
	
	# Quick calculations line 22-24
	if ip == 21:
		if code[21:24] == [
			"inc a"
			"inc d"
			"jnz d -2"]:
			result = reg["a"] + reg["d"]
			reg.update({"a": result})
			reg.update({"d": 0})
			ip = 24
			continue
	
	if args[0] == "inc":
		reg.update({args[1]: reg[args[1]] + 1})
		ip += 1
	elif args[0] == "dec":
		reg.update({args[1]: reg[args[1]] - 1})
		ip += 1
	elif args[0] == "tgl":
		try:
			index = ip + parse(args[1])
			tgl_args = code[index].split()
			tgl_args[0] = toggle_op_codes[tgl_args[0]]
			new_command = " ".join(tgl_args)
			code[index] = new_command
		except:
			pass
		
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

for r in sorted(reg.keys()):
	print(f"{r} = {reg[r]}")