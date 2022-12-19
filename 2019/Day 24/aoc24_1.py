file = open("aoc24_input.txt")
l = file.read().split("\n")
file.close()

g = [[0 for _ in range(5)] for _ in range(5)]

for iy in range(5):
    for ix in range(5):
        g[iy][ix] = int(l[iy][ix] == "#")

seen = set()

while 1:
    state = "".join("".join(str(tile) for tile in row) for row in g)
    if state in seen:
        print(int(state[::-1], 2))
        break
    seen.add(state)

    ng = [[0 for _ in range(5)] for _ in range(5)]
    for iy in range(5):
        for ix in range(5):
            c = 0
            
            if ix > 0:
                c += g[iy][ix-1]
            if ix < 4:
                c += g[iy][ix+1]
            if iy > 0:
                c += g[iy-1][ix]
            if iy < 4:
                c += g[iy+1][ix]
            
            if g[iy][ix] == 0:
                if 1 <= c <= 2:
                    ng[iy][ix] = 1
            else:
                if c == 1:
                    ng[iy][ix] = 1
    
    g = ng