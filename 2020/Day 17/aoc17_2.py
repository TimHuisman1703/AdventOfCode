file = open("aoc17_input.txt")
l = file.read().split("\n")
file.close()

def get_neighbors(g, x, y, z, w):
    c = 0
    for dw in range(-1, 2):
        if w+dw < 0 or w+dw > len(g)-1:
            continue
        for dz in range(-1, 2):
            if z+dz < 0 or z+dz > len(g[0])-1:
                continue
            for dy in range(-1, 2):
                if y+dy < 0 or y+dy > len(g[0][0])-1:
                    continue
                for dx in range(-1, 2):
                    if x+dx < 0 or x+dx > len(g[0][0][0])-1:
                        continue
                    if dx == dy == dz == dw == 0:
                        continue
                    if g[w+dw][z+dz][y+dy][x+dx]:
                        c += 1
    return c

cycles = 6
dim_x = 2*cycles+2+len(l[0])
dim_y = 2*cycles+2+len(l)
dim_z = 2*cycles+2+1
dim_w = 2*cycles+2+1
g = [[[[0 for ix in range(dim_x)] for iy in range(dim_y)] for iz in range(dim_z)] for iw in range(dim_w)]

for iy in range(len(l)):
    for ix in range(len(l[0])):
        g[(dim_w-1)//2][(dim_z-1)//2][cycles+1+iy][cycles+1+ix] = int(l[iy][ix] == "#")

for i in range(cycles):
    n = [[[[0 for ix in range(dim_x)] for iy in range(dim_y)] for iz in range(dim_z)] for iw in range(dim_w)]
    for iw in range(dim_w):
        for iz in range(dim_z):
            for iy in range(dim_y):
                for ix in range(dim_x):
                    p = get_neighbors(g, ix, iy, iz, iw)
                    if p == 2:
                        n[iw][iz][iy][ix] = g[iw][iz][iy][ix]
                    elif p == 3:
                        n[iw][iz][iy][ix] = 1
    g = n
print(sum(sum(sum(sum(ix) for ix in iy) for iy in iz) for iz in g))