file = open("aoc22_input.txt")
l = file.read().split("\n")
file.close()

g = [[(0, -1) for _ in range(10)] for _ in range(10)]

bricks = []
for w in l:
    a, b = w.split("~")
    a = [int(j) for j in a.split(",")]
    b = [int(j) for j in b.split(",")]

    bricks.append((a, b))

bricks = sorted(bricks, key=lambda x: x[0][2])

on = [[] for _ in range(len(bricks))]
for i in range(len(bricks)):
    a, b = bricks[i]

    height = 0
    curr_on = set()
    for iy in range(a[1], b[1] + 1):
        for ix in range(a[0], b[0] + 1):
            h, idx = g[iy][ix]
            if h > height:
                height = h
                curr_on = set()
            if h == height:
                curr_on.add(idx)
    on[i] = curr_on

    diff = a[2] - height
    a[2] -= diff
    b[2] -= diff

    for iy in range(a[1], b[1] + 1):
        for ix in range(a[0], b[0] + 1):
            g[iy][ix] = (b[2] + 1, i)

base = set()
for s in on:
    if len(s) == 1:
        x = s.pop()
        if x > -1:
            base.add(x)

print(len(bricks) - len(base))