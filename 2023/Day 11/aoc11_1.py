file = open("aoc11_input.txt")
l = file.read().split("\n")
file.close()

g = [[l[iy][ix] == "#" for ix in range(len(l[0]))] for iy in range(len(l))]

ng = [[] for _ in range(len(g))]
for ix in range(len(g[0])):
    for iy in range(len(g)):
        ng[iy].append(g[iy][ix])
    if not any(g[iy][ix] for iy in range(len(g))):
        for iy in range(len(g)):
            ng[iy].append(False)
g = ng

ng = []
for iy in range(len(g)):
    ng.append(g[iy])
    if not any(g[iy]):
        ng.append(g[iy][:])
g = ng

ps = []
s = 0
for iy in range(len(g)):
    for ix in range(len(g[0])):
        if g[iy][ix]:
            for jx, jy in ps:
                s += abs(jx - ix) + abs(jy - iy)
            ps.append((ix, iy))

print(s)