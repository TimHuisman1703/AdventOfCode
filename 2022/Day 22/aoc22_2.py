file = open("aoc22_input.txt")
l = file.read().split("\n")
file.close()

size = 50
pos = [(1, 0), (2, 0), (1, 1), (0, 2), (1, 2), (0, 3)]
off = [
    [(1, 0), (2, 1), (3, 0), (5, 0)],
    [(4, 2), (2, 2), (0, 2), (5, 3)],
    [(1, 3), (4, 1), (3, 1), (0, 3)],
    [(4, 0), (5, 1), (0, 0), (2, 0)],
    [(1, 2), (5, 2), (3, 2), (2, 3)],
    [(4, 3), (1, 1), (0, 1), (3, 3)],
]

def belongs_to(x, y):
    for i in range(len(pos)):
        ix, iy = pos[i]
        if size * ix <= x < size * (ix + 1) and size * iy <= y < size * (iy + 1):
            return i
    return -1

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
            nx = x + (d == 0) - (d == 2)
            ny = y + (d == 1) - (d == 3)
            nd = d

            if belongs_to(nx, ny) == -1:
                f = belongs_to(x, y)
                nf, nd = off[f][d]
                nx = nx % size
                ny = ny % size

                for _ in range((nd - d) % 4):
                    nx, ny = (size - 1 - ny), nx

                nx += pos[nf][0] * size
                ny += pos[nf][1] * size

            if g[ny][nx] == "#":
                break
            x = nx
            y = ny
            d = nd

print(1000 * (y + 1) + 4 * (x + 1) + d)