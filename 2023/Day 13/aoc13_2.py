file = open("aoc13_input.txt")
l = file.read().split("\n\n")
file.close()

s = 0
for g in l:
    g = g.split("\n")

    for mult in [1, 100]:
        g = [[g[iy][ix] for iy in range(len(g))] for ix in range(len(g[0]))]

        for iy in range(1, len(g)):
            a = iy - 1
            b = iy
            diff = 0
            while a >= 0 and b < len(g):
                diff += sum(g[a][j] != g[b][j] for j in range(len(g[a])))
                if diff > 1:
                    break
                a -= 1
                b += 1
            else:
                s += iy * mult * diff

print(s)