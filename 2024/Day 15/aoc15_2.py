file = open("aoc15_input.txt")
g, instrs = file.read().split("\n\n")
file.close()

g = [[*row] for row in g.split("\n")]
ng = []
for iy in range(len(g)):
    row = []
    for ix in range(len(g[0])):
        if g[iy][ix] == "@":
            x, y = 2 * ix, iy
            g[iy][ix] = "."
        
        if g[iy][ix] == ".":
            row.extend([".", "."])
        elif g[iy][ix] == "#":
            row.extend(["#", "#"])
        elif g[iy][ix] == "O":
            row.extend(["[", "]"])
    ng.append(row)
g = ng

for c in instrs:
    dx = (c == ">") - (c == "<")
    dy = (c == "v") - (c == "^")

    if g[y + dy][x + dx] == "#":
        continue
    
    btm = []
    if g[y + dy][x + dx] == "[":
        btm.append((x + dx, y + dy))
    elif g[y + dy][x + dx] == "]":
        btm.append((x + dx - 1, y + dy))

    i = 0
    while i < len(btm):
        bx, by = btm[i]
        i += 1

        if dx < 0:
            cc = g[by][bx - 1]
            if cc == "#":
                break
            elif cc == "]":
                btm.append((bx - 2, by))
        elif dx > 0:
            cc = g[by][bx + 2]
            if cc == "#":
                break
            elif cc == "[":
                btm.append((bx + 2, by))
        else:
            if g[by + dy][bx] == "#" or g[by + dy][bx + 1] == "#":
                break
            if g[by + dy][bx] == "]":
                btm.append((bx - 1, by + dy))
            if g[by + dy][bx] == "[":
                btm.append((bx, by + dy))
            if g[by + dy][bx + 1] == "[":
                btm.append((bx + 1, by + dy))
    else:
        x += dx
        y += dy
        for bx, by in btm:
            g[by][bx] = "."
            g[by][bx + 1] = "."
        for bx, by in btm:
            g[by + dy][bx + dx] = "["
            g[by + dy][bx + dx + 1] = "]"

r = 0
for iy in range(len(g)):
    for ix in range(len(g[0])):
        if g[iy][ix] == "[":
            r += iy * 100 + ix

print(r)