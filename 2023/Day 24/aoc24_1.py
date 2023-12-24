file = open("aoc24_input.txt")
l = file.read().split("\n")
file.close()

import numpy as np

stones = []
for w in l:
    p, v = w.split(" @ ")

    p = [int(j) for j in p.split(", ")]
    v = [int(j) for j in v.split(", ")]

    stones.append((p, v))

s = 0
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        a = stones[i]
        b = stones[j]

        A = np.array([
            [a[1][0], -b[1][0]],
            [a[1][1], -b[1][1]],
        ])
        B = np.array([
            [-a[0][0] + b[0][0]],
            [-a[0][1] + b[0][1]],
        ])

        try:
            t = np.linalg.solve(A, B)
        except:
            continue

        if t[0][0] < 0 or t[1][0] < 0:
            continue

        p = [a[1][j] * t[0][0] + a[0][j] for j in range(2)]

        bottom = 200000000000000
        top = 400000000000000
        if bottom <= p[0] <= top and bottom <= p[1] <= top:
            s += 1

print(s)