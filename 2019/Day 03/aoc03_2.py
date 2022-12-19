file = open("aoc03_input.txt")
l = file.read().split("\n")
file.close()

w = [l[j].split(",") for j in range(2)]

segments = []
x = y = l = 0
for instr in w[0]:
    d, strength = instr[0], int(instr[1:])
    nx = x + (int(d == "R") - int(d == "L")) * strength
    ny = y + (int(d == "D") - int(d == "U")) * strength
    
    if x == nx:
        segments.append((x, (y, ny), l))
    if y == ny:
        segments.append(((x, nx), y, l))

    x, y = nx, ny
    l += strength

possible = set()

x = y = l = 0
for instr in w[1]:
    d, strength = instr[0], int(instr[1:])
    nx = x + (int(d == "R") - int(d == "L")) * strength
    ny = y + (int(d == "D") - int(d == "U")) * strength

    if x == nx:
        cx, cy = x, (min(y, ny), max(y, ny))
        for tx, ty, tl in segments:
            if type(tx) == int:
                sx, sy = tx, (min(ty), max(ty))
                if cx == sx and cy[0] <= sy[1] and sy[0] <= cy[1]:
                    px, py = cx, min(cy[0], sy[0])
                    pl = l + abs(py - y) + tl + abs(ty[0] - y)
                    possible.add((px, py, pl))
                    px, py = cx, max(cy[0], sy[0])
                    pl = l + abs(py - y) + tl + abs(ty[0] - y)
                    possible.add((px, py, pl))
            else:
                sx, sy = (min(tx), max(tx)), ty
                if sx[0] <= cx and cx <= sx[1] and cy[0] <= sy and sy <= cy[1]:
                    px, py = cx, sy
                    pl = l + abs(py - y) + tl + abs(tx[0] - x)
                    possible.add((px, py, pl))
    else:
        cx, cy = (min(x, nx), max(x, nx)), y
        for tx, ty, tl in segments:
            if type(tx) == int:
                sx, sy = tx, (min(ty), max(ty))
                if cx[0] <= sx and sx <= cx[1] and sy[0] <= cy and cy <= sy[1]:
                    px, py = sx, cy
                    pl = l + abs(px - x) + tl + abs(ty[0] - y)
                    possible.add((px, py, pl))
            else:
                sx, sy = (min(tx), max(tx)), ty
                if cy == sy and cx[0] <= sx[1] and sx[0] <= cx[1]:
                    px, py = min(cx[0], sx[0]), cy
                    pl = l + abs(px - x) + tl + abs(tx[0] - x)
                    possible.add((px, py, pl))
                    px, py = max(cx[0], sx[0]), cy
                    pl = l + abs(px - x) + tl + abs(tx[0] - x)
                    possible.add((px, py, pl))

    x, y = nx, ny
    l += strength

steps = 1e100
for p in possible:
    curr = p[2]
    if curr < 10000: # meh
        continue

    if curr < steps:
        steps = curr

print(steps)