file = open("aoc21_input.txt")
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

r = [15615244] + [0] * 5

steps = 0
while r[ip] < len(code):
	steps += 1
	op, a, b, c = code[r[ip]].split()
	a, b, c = int(a), int(b), int(c)
	r = execute(op, a, b, c, r)
	r[ip] += 1

print(f"a = {r[0]} -> {steps} steps")

# I guess it's a sort of hashing function?
#
# #ip 2
# 0		seti 123 0 5					f = 123
# 1		bani 5 456 5					f = f & 456
# 2		eqri 5 72 5						f = (f == 72) = (f == (123 & 456))
# 3		addr 5 2 2						if (123 & 456) != 72:
# 4			seti 0 0 2						go back to the start (shouldn't happen)
# 5		seti 0 4 5						f = 0
# 6		bori 5 65536 4					e = f | 65536 = 65536
# 7		seti 15466939 9 5				f = 15466939
# 8		bani 4 255 3					d = e & 255 (= 0) (= 0) (= 1)
# 9		addr 5 3 5						f = f + d (= 15466939 + 0 = 15466939) (= 6386729 + 0 = 6386729) (= 5813795 + 1 = 5813796)
# 10	bani 5 16777215 5				f = f & 16777215 (= 15466939 & 16777215 = 15466939) (= 6386729 & 16777215 = 6386729) (= 5813796 & 16777215 = 5813796)
# 11	muli 5 65899 5					f = f * 65899 (= 15466939 * 65899 = 1019255813161) (= 6386729 * 65899 = 420879054371) (= 5813796 * 65899 = 383123342604)
# 12	bani 5 16777215 5				f = f & 16777215 (= 1019255813161 & 16777215 = 6386729) (= 420879054371 & 16777215 = 5813795) (= 420879054371 & 16777215 = 15615244)
# 13	gtir 256 4 3					...
# 14	addr 3 2 2						if e (= 65536) (= 256) (= 1) < 256:
# 15	addi 2 1 2							...
# 16		seti 27 8 2						jump to line 28
# 17	seti 0 7 3						d = 0
# 18	addi 3 1 1						b = d + 1
# 19	muli 1 256 1					b = b * 256
# 20	gtrr 1 4 1						...
# 21	addr 1 2 2						if b (= 256) > e (= 65536) (= 256)		(first time loops until d == 256, second time loops until d == 1)
# 22	addi 2 1 2							...
# 23	seti 25 2 2							jump to line 26
# 24	addi 3 1 3						d = d + 1
# 25	seti 17 7 2						jump to line 18
# 26	setr 3 7 4						e = d (= 256) (= 1)
# 27	seti 7 3 2						jump to line 8
# 28	eqrr 5 0 3						...
# 29	addr 3 2 2						if f (= 15615244) != a:
# 30	seti 5 9 2							jump to line 6