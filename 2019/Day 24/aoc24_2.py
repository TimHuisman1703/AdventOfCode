file = open("aoc24_input.txt")
l = file.read().split("\n")
file.close()

STEPS = 200

g = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(1 + STEPS)]

for iy in range(5):
    for ix in range(5):
        g[0][iy][ix] = int(l[iy][ix] == "#")

def count_neighbors(g, x, y, level):
    c = 0

    if x == 0:
        c += g[level-1][2][1]
    elif x == 3 and y == 2:
        for iy in range(5):
            c += g[level+1][iy][4]
    else:
        c += g[level][y][x-1]
    
    if x == 4:
        c += g[level-1][2][3]
    elif x == 1 and y == 2:
        for iy in range(5):
            c += g[level+1][iy][0]
    else:
        c += g[level][y][x+1]

    if y == 0:
        c += g[level-1][1][2]
    elif y == 3 and x == 2:
        for ix in range(5):
            c += g[level+1][4][ix]
    else:
        c += g[level][y-1][x]
    
    if y == 4:
        c += g[level-1][3][2]
    elif y == 1 and x == 2:
        for ix in range(5):
            c += g[level+1][0][ix]
    else:
        c += g[level][y+1][x]
    
    return c

for steps in range(STEPS):
    ng = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(1 + STEPS)]
    for level in range(-STEPS // 2, STEPS // 2 + 1):
        for iy in range(5):
            for ix in range(5):
                if iy == ix == 2:
                    continue

                c = count_neighbors(g, ix, iy, level)
                
                if g[level][iy][ix] == 0:
                    if 1 <= c <= 2:
                        ng[level][iy][ix] = 1
                else:
                    if c == 1:
                        ng[level][iy][ix] = 1
    
    g = ng

print(sum(sum(sum(row) for row in level) for level in g))