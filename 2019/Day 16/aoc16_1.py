file = open("aoc16_input.txt")
s = file.read()
file.close()

import numpy as np

STEPS = 100

n = len(s)
v = np.array([int(j) for j in s])
v.resize((n, 1))

M = np.zeros((n, n), int)
for iy in range(n):
	for ix in range(n):
		i = (ix + 1) // (iy + 1)
		M[iy, ix] = (i % 4 == 1) - (i % 4 == 3)

for _ in range(STEPS):
	v = abs(M @ v) % 10

print("".join(str(j) for j in v.flatten()[:8]))