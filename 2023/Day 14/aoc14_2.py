file = open("aoc14_input.txt")
g = file.read().split("\n")
file.close()

seen = {}

idx = 0
while idx < 10 ** 9:
    for _ in range(4):
        ng = [[".#"[g[iy][ix] == "#"] for ix in range(len(g[0]))] for iy in range(len(g))]

        s = 0
        for ix in range(len(g[0])):
            y = 0
            for iy in range(len(g)):
                if g[iy][ix] == "#":
                    y = iy + 1
                if g[iy][ix] == "O":
                    ng[y][ix] = "O"
                    y += 1

        g = [[ng[len(g) - 1 - iy][ix] for iy in range(len(ng))] for ix in range(len(ng[0]))]

    idx += 1
    key = "".join("".join(row) for row in g)

    if key in seen:
        loop = idx - seen[key]
        if (10 ** 9 - idx) % loop == 0:
            break

    seen[key] = idx

s = 0
for iy in range(len(g)):
    for ix in range(len(g[0])):
        if g[iy][ix] == "O":
            s += len(g) - iy

print(s)