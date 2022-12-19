file = open("aoc18_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

width = 100
height = 100
turns = 100

def count_neighbors(g, ix, iy):
    c = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dx == dy == 0:
                continue
            if -1 < iy+dy < len(g) and -1 < ix+dx < len(g[0]):
                c += g[iy+dy][ix+dx]
    return c

born = [0, 0, 0, 1, 0, 0, 0, 0, 0]
survive = [0, 0, 1, 1, 0, 0, 0, 0, 0]

g = [[1 if ix == "#" else 0 for ix in iy] for iy in l]

for i in range(turns):
    ng = [[0 for ix in range(width)] for iy in range(height)]
    for iy in range(height):
        for ix in range(width):
            p = count_neighbors(g, ix, iy)
            ng[iy][ix] = int(g[iy][ix] * survive[p] + (1-g[iy][ix]) * born[p])
    g = ng

print(sum(sum(iy) for iy in g))