file = open("aoc22_input.txt")
l = file.read().split("\n")
file.close()

def pow(a, b, mod):
	if a < 2:
		return a
	if b == 0:
		return 1
	
	if b % 2 == 0:
		c = pow(a, b // 2, mod)
		return c * c % mod
	else:
		return a * pow(a, b - 1, mod) % mod

def geom_series(r, n, mod):
	if n == 1:
		return 1
	
	if n % 2 == 0:
		return (1 + r) * geom_series(r * r % mod, n // 2, mod) % mod
	else:
		return (1 + r * geom_series(r, n - 1, mod)) % mod

CARDS = 119315717514047
N = 101741582076661

goes_to = []
for j in range(2):
	pos = j
	for i in l:
		if i.startswith("deal into"):
			pos = CARDS - 1 - pos
		elif i.startswith("cut"):
			a = int(i.split()[-1])
			pos = (pos - a) % CARDS
		else:
			a = int(i.split()[-1])
			pos = (pos * a) % CARDS
	goes_to.append(pos)
r, c = (goes_to[1] - goes_to[0]) % CARDS, goes_to[0]

geom_sum = geom_series(r, N, CARDS)
r_to_nth = pow(r, N, CARDS)

goes_to = []
for i in range(2):
	goes_to.append((c * geom_sum + r_to_nth * i) % CARDS)
r, c = (goes_to[1] - goes_to[0]) % CARDS, goes_to[0]


print("Put this in a congruence solver:")
print(f"({r} * k + {c}) % {CARDS} == 2020")