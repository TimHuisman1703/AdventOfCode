file = open("aoc03_input.txt")
l = file.read().split("\n")
file.close()

g = [[0 for _ in range(1000)] for _ in range(1000)]
solo = []

for s in l:
    args = s.split()

    id = int(args[0][1:])
    x, y = [int(j) for j in args[2][:-1].split(",")]
    w, h = [int(j) for j in args[3].split("x")]
    
    alone = True
    for iy in range(y, y+h):
        for ix in range(x, x+w):
            if g[iy][ix] > 0:
                alone = False
                if g[iy][ix] in solo:
                    solo.remove(g[iy][ix])
            g[iy][ix] = id
    
    if alone:
        solo.append(id)

print(*solo)