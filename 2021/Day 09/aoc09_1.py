file = open("aoc09_input.txt")
l = file.read().split("\n")
file.close()

import numpy as np

l = np.array([[int(j) for j in row] for row in l])
c = 0

for iy in range(len(l)):
    for ix in range(len(l[0])):
        x0, x1 = max(0, ix - 1), min(len(l[0]), ix + 2)
        y0, y1 = max(0, iy - 1), min(len(l), iy + 2)

        if min(l[y0:y1, x0:x1].flatten()) == l[iy, ix]:
            c += 1 + l[iy, ix]

print(c)