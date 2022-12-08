file = open("aoc08_input.txt")
g = [[int(j) for j in row] for row in file.read().split("\n")]
file.close()

m = 0
for iy in range(len(g)):
    for ix in range(len(g[0])):
        p = 1

        for i in range(4):
            x, y = ix, iy
            c = 0

            while 1:
                x += (i == 0) - (i == 2)
                y += (i == 1) - (i == 3)

                if x < 0 or x >= len(g[0]) or y < 0 or y >= len(g):
                    break

                c += 1
                if g[y][x] >= g[iy][ix]:
                    break

            p *= c

        m = max(p, m)

print(m)