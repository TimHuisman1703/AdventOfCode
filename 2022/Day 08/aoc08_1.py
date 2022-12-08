file = open("aoc08_input.txt")
g = [[[int(j), 0] for j in row] for row in file.read().split("\n")]
file.close()

for i in range(4):
    for iy in range(len(g)):
        m = -1
        for ix in range(len(g[0])):
            if g[iy][ix][0] > m:
                g[iy][ix][1] = 1
                m = g[iy][ix][0]
    
    g = [[g[ix][len(g) - 1 - iy] for ix in range(len(g[0]))] for iy in range(len(g))]

print(sum(sum([j[1] for j in row]) for row in g))