file = open("aoc19_input.txt")
code = file.read().split("\n")
file.close()

def execute(op, a, b, c, r):
	if op == "addr":
		r[c] = r[a] + r[b]
	elif op == "addi":
		r[c] = r[a] + b
	elif op == "mulr":
		r[c] = r[a] * r[b]
	elif op == "muli":
		r[c] = r[a] * b
	elif op == "banr":
		r[c] = r[a] & r[b]
	elif op == "bani":
		r[c] = r[a] & b
	elif op == "borr":
		r[c] = r[a] | r[b]
	elif op == "bori":
		r[c] = r[a] | b
	elif op == "setr":
		r[c] = r[a]
	elif op == "seti":
		r[c] = a
	elif op == "gtir":
		r[c] = int(a > r[b])
	elif op == "gtri":
		r[c] = int(r[a] > b)
	elif op == "gtrr":
		r[c] = int(r[a] > r[b])
	elif op == "eqir":
		r[c] = int(a == r[b])
	elif op == "eqri":
		r[c] = int(r[a] == b)
	elif op == "eqrr":
		r[c] = int(r[a] == r[b])
	
	return r

ip = code.pop(0)
ip = int(ip.split()[-1])

r = [0] * 6

while r[ip] < len(code):
	op, a, b, c = code[r[ip]].split()
	a, b, c = int(a), int(b), int(c)
	r = execute(op, a, b, c, r)
	r[ip] += 1

print(r[0])