file = open("aoc04_input.txt")
g = file.read().split("\n")
file.close()

w, h = len(g[0]), len(g)

r = 0
for iy in range(h):
    for ix in range(w):
        if g[iy][ix] != "@":
            continue

        s = 0
        for jy in range(iy - 1, iy + 2):
            for jx in range(ix - 1, ix + 2):
                if ix == jx and iy == jy:
                    continue
                if jx < 0 or jx >= w or jy < 0 or jy >= h:
                    continue
                if g[jy][jx] == "@":
                    s += 1

        r += s < 4

print(r)