file = open("aoc11_input.txt")
l = file.read().split("\n")
file.close()

g = [[l[iy][ix] == "#" for ix in range(len(l[0]))] for iy in range(len(l))]

xs = []
for ix in range(len(g[0])):
    if not any(g[iy][ix] for iy in range(len(g))):
        xs.append(ix)

ys = []
for iy in range(len(g)):
    if not any(g[iy]):
        ys.append(iy)

ps = []
s = 0
for iy in range(len(g)):
    for ix in range(len(g[0])):
        if g[iy][ix]:
            for jx, jy in ps:
                s += abs(jx - ix) + abs(jy - iy)
                s += 999999 * sum(iy < y < jy or jy < y < iy for y in ys)
                s += 999999 * sum(ix < x < jx or jx < x < ix for x in xs)
            ps.append((ix, iy))

print(s)