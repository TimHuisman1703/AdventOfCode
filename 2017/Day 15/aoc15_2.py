file = open("aoc15_input.txt")
l = file.read().split("\n")
file.close()

AMOUNT = 5000000

a, b = int(l[0].split()[4]), int(l[1].split()[4])

la, lb = [], []

m = 0
passed = 0
while min(len(la), len(lb)) <= AMOUNT:
	a = (a * 16807) % 2147483647
	b = (b * 48271) % 2147483647

	if a & 0b11 == 0:
		la.append(a)
	if b & 0b111 == 0:
		lb.append(b)
	
	m = min(len(la), len(lb))
	if m % 100000 == 99999 and passed != m:
		passed = m
		print(f"Passed {m+1}")

c = 0
mask = 2**16 - 1
for i in range(AMOUNT):
	if la[i] & mask == lb[i] & mask:
		c += 1

print(c)