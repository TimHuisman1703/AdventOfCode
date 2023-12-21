file = open("aoc21_input.txt")
g = file.read().split("\n")
file.close()

p = set()
walls = set()
for iy in range(len(g)):
    for ix in range(len(g[0])):
        if g[iy][ix] == "S":
            p.add((ix, iy))
        if g[iy][ix] == "#":
            walls.add((ix, iy))

for _ in range(64):
    np = set()
    for x, y in p:
        for d in range(4):
            nx = x + (d == 0) - (d == 1)
            ny = y + (d == 2) - (d == 3)

            key = (nx, ny)
            if key not in walls:
                np.add(key)

    p = np

print(len(p))