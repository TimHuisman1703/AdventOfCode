file = open("aoc22_input.txt")
l = file.read().split("\n")
file.close()

g = []
for iy in range(len(l) - 2):
    g.append(l[iy])

instr = l[-1]
i = 0

x = g[0].find(".")
y = 0
d = 0

while i < len(instr):
    if instr[i] == "L":
        d = (d - 1) % 4
        i += 1
    elif instr[i] == "R":
        d = (d + 1) % 4
        i += 1
    else:
        s = i
        while i < len(instr) and instr[i].isdigit():
            i += 1
        n = int(instr[s:i])
        for _ in range(n):
            if d == 0:
                nx = x + 1
                if nx >= len(g[y]):
                    nx = 0
                    while g[y][nx] == " ":
                        nx += 1
                if g[y][nx] == "#":
                    break
                x = nx
            elif d == 1:
                ny = y + 1
                while ny >= len(g) or x >= len(g[ny]) or g[ny][x] == " ":
                    ny = 0
                    while ny >= len(g) or x >= len(g[ny]) or g[ny][x] == " ":
                        ny += 1
                if g[ny][x] == "#":
                    break
                y = ny
            elif d == 2:
                nx = x - 1
                if nx < 0 or g[y][nx] == " ":
                    nx = len(g[y]) - 1
                if g[y][nx] == "#":
                    break
                x = nx
            elif d == 3:
                ny = y - 1
                if ny < 0 or x >= len(g[ny]) or g[ny][x] == " ":
                    ny = len(g) - 1
                    while x >= len(g[ny]) or g[ny][x] == " ":
                        ny -= 1
                if g[ny][x] == "#":
                    break
                y = ny

print(1000 * (y + 1) + 4 * (x + 1) + d)