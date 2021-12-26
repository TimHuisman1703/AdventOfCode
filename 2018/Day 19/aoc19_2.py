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

def get_prime_factors(n):
	p = []
	while n % 2 == 0:
		n //= 2
		p.append(2)
	
	d = 3
	while d * d <= n:
		if n % d == 0:
			n //= d
			p.append(d)
		else:
			d += 2
	
	if n > 1:
		p.append(n)
	
	return p

ip = code.pop(0)
ip = int(ip.split()[-1])

r = [1] + [0] * 5

while r[ip] != 1:
	op, a, b, c = code[r[ip]].split()
	a, b, c = int(a), int(b), int(c)
	r = execute(op, a, b, c, r)
	r[ip] += 1

p = get_prime_factors(r[4])

s = set()
for i in range(1 << len(p)):
	a = 1
	for j in range(len(p)):
		if (i >> j) & 1:
			a *= p[j]
	s.add(a)

print(sum(s))

# This program calculates all divisors of e (the fifth register) and returns their sum
#
# #ip 1
# 0		addi 1 16 1
# 1			seti 1 1 5						f = 1 (initialize for-loop)
# 2				seti 1 4 2					c = 1 (initialize for-loop)
# 3					mulr 5 2 3				...
# 4					eqrr 3 4 3				...
# 5					addr 3 1 1				if f * c == e:
# 6					addi 1 1 1					...
# 7					addr 5 0 0					a += f
# 8					addi 2 1 2				c += 1
# 9					gtrr 2 4 3				...
# 10				addr 1 3 1				if c <= e:
# 11				seti 2 7 1					repeat loop
# 12			addi 5 1 5					f += 1
# 13			gtrr 5 4 3					...
# 14			addr 3 1 1					if f <= e:
# 15			seti 1 8 1						repeat loop
# 16		mulr 1 1 1						ip = ip * ip (ip = 256, terminate program)
# 17	addi 4 2 4							e = e + 2 = 0 + 2 = 2
# 18	mulr 4 4 4							e = e * e = 2 * 2 = 4
# 19	mulr 1 4 4							e = e * ip = e * 19 = 4 * 19 = 76
# 20	muli 4 11 4							e = e * 11 = 76 * 11 = 836
# 21	addi 3 1 3							d = d + 1 = 0 + 1 = 1
# 22	mulr 3 1 3							d = d * ip = d * 22 = 1 * 22 = 22
# 23	addi 3 3 3							d = d + 3 = 22 + 3 = 25
# 24	addr 4 3 4							e = e + d = 836 + 25 = 861
# 25	addr 1 0 1							if doing part 1:
# 26		seti 0 3 1							immediately go into the double for-loop above
# 27	setr 1 1 3							d = ip = 27
# 28	mulr 3 1 3							d = d * ip = d * 28 = 27 * 28 = 756
# 29	addr 1 3 3							d = d + ip = d + 29 = 756 + 29 = 785
# 30	mulr 1 3 3							d = d * ip = d * 30 = 785 * 30 = 23550
# 31	muli 3 14 3							d = d * 14 = 23550 * 14 = 329700
# 32	mulr 3 1 3							d = d * ip = d * 32 = 329700 * 32 = 10550400
# 33	addr 4 3 4							e = e + d = 861 + 10550400 = 10551261
# 34	seti 0 9 0							a = 0
# 35	seti 0 4 1							enter double for-loop