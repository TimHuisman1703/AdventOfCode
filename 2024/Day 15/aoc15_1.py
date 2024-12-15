file = open("aoc15_input.txt")
g, instrs = file.read().split("\n\n")
file.close()

g = [[*row] for row in g.split("\n")]
for iy in range(len(g)):
    for ix in range(len(g[0])):
        if g[iy][ix] == "@":
            x, y = ix, iy
            g[iy][ix] = "."

for c in instrs:
    dx = (c == ">") - (c == "<")
    dy = (c == "v") - (c == "^")

    cx, cy = x, y
    while g[cy][cx] != "#":
        cx += dx
        cy += dy

        if g[cy][cx] == ".":
            g[cy][cx] = "O"
            g[y + dy][x + dx] = "."
            x += dx
            y += dy
            break

r = 0
for iy in range(len(g)):
    for ix in range(len(g[0])):
        if g[iy][ix] == "O":
            r += iy * 100 + ix

print(r)