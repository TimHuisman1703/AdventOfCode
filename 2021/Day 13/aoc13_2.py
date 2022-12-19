file = open("aoc13_input.txt")
l = file.read().split("\n")
file.close()

c = []
s = 0
for i in range(len(l)):
    if l[i] == "":
        s = i + 1
        break
    
    a, b = [int(j) for j in l[i].split(",")]
    c += [(a, b)]

for i in range(s, len(l)):
    instr = l[i].split()[2]
    hori = instr[0] == "x"
    val = int(instr[2:])

    if hori:
        c = [(-abs(j[0] - val) + val, j[1]) for j in c]
    else:
        c = [(j[0], -abs(j[1] - val) + val) for j in c]

c = set(c)

min_x, min_y, max_x, max_y = 10000, 10000, -10000, -10000
for x, y in c:
    min_x = min(x, min_x)
    min_y = min(y, min_y)
    max_x = max(x, max_x)
    max_y = max(y, max_y)

g = [["." for jx in range(max_x - min_x + 1)] for jy in range(max_y - min_y + 1)]

for a, b in c:
    g[b - min_y][a - min_x] = "#"

print("\n".join("".join(row) for row in g))