file = open("aoc16_input.txt")
s = file.read()
file.close()

STEPS = 100

n = len(s)
offset = int(s[:7])
m = 10000 * n - offset

l = [0] * m
for i in range(m):
	l[i] = int(s[(offset + i) % n])

for steps in range(STEPS):
	for i in range(m - 2, -1, -1):
		l[i] = (l[i] + l[i+1]) % 10

print(*l[:8], sep="")