file = open("aoc14_input.txt")
g = file.read().split("\n")
file.close()

s = 0
for ix in range(len(g[0])):
    y = 0
    for iy in range(len(g)):
        if g[iy][ix] == "#":
            y = iy + 1
        if g[iy][ix] == "O":
            s += len(g) - y
            y += 1

print(s)