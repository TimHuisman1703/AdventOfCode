file = open("aoc20_input.txt")
p = int(file.read())
file.close()

primes = []

def get_first_prime(n):
	global primes

	for i in primes:
		if n % i == 0:
			return i
	
	primes.append(n)
	return n

def prime_divide(b, i):
	a = 1
	while b % i == 0:
		a *= i
		b //= i
	return a, b

p //= 10
d = {1: 1}
m = 0

i = 1
while d[i] < p:
	i += 1

	div = get_first_prime(i)
	if div == i:
		d[i] = 1 + i
	else:
		a, b = prime_divide(i, div)
		if b > 1:
			d[i] = d[a] * d[b]
		else:
			d[i] = d[a // div] * div + 1
	
	if d[i] > m:
		m = d[i]
	if i % 10000 == 0:
		print(i, d[i], m)

print(i)