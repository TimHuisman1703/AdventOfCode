file = open("aoc04_input.txt")
g = file.read().split("\n")
file.close()

r = 0
for iy in range(1, len(g) - 1):
    for ix in range(1, len(g[0])- 1):
        if g[iy][ix] == "A":
            l = [
                g[iy - 1][ix - 1],
                g[iy - 1][ix + 1],
                g[iy + 1][ix + 1],
                g[iy + 1][ix - 1],
            ]
            r += "".join(l) in ["MSSM", "SMMS", "MMSS", "SSMM"]

print(r)