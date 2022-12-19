file = open("aoc20_input.txt")
l = file.read().split("\n")
file.close()

import re

def rotate_string_square_cw(sl, dim, amount):
    if amount == 0:
        return sl
    
    nsl = []
    for i in range(dim):
        cs = ""
        for j in range(dim):
            cs = sl[j][i] + cs
        nsl.append(cs)
    return rotate_string_square_cw(nsl, dim, amount-1)

def mirror_string_square(sl, dim):
    nsl = []
    for i in range(dim):
        nsl.append(sl[i][::-1])
    return nsl

dim = 10

layout = {}
edges = {}

i = -1
while i < len(l)-1:
    i += 1
    tile_id = int(l[i].split()[1][:-1])
    
    i += 1
    normal = []
    cl = []
    for j in range(dim):
        cl.append(l[i])
        normal.append(int(l[i].replace("#", "1").replace(".", "0"), 2))
        i += 1
    layout.setdefault(tile_id, cl)
    
    rotated = [0]*dim
    for j in range(dim):
        for k in range(len(normal)):
            rotated[j] += ((normal[k] >> (dim-1-j)) & 1) << (dim-1-k)
    
    edge = [normal[0], -1, -1, rotated[-1], -1, rotated[0], normal[-1], -1]
    for j in [1, 2, 4, 7]:
        n = 0
        for k in range(dim):
            n += ((edge[(j+4)%8] >> k) & 1) << (dim - k - 1)
        edge[j] = n
    
    edges.setdefault(tile_id, edge)

neighbors = {}

for i in edges.keys():
    neigh = set()
    for j in edges.keys():
        if i == j:
            continue
        for k in edges[i]:
            if k in edges[j]:
                neigh.add(j)
    neighbors.setdefault(i, neigh)

grid_dim = round(len(edges.keys())**0.5)
grid = [[0 for i in range(grid_dim)] for j in range(grid_dim)]
available = [i for i in neighbors.keys()]
for i in available:
    if len(neighbors[i]) == 2:
        grid[0][0] = i
        available.remove(i)
        break

for i in range(1, grid_dim):
    for j in neighbors[grid[0][i-1]]:
        if len(neighbors[j]) < 4 and j in available:
            grid[0][i] = j
            available.remove(j)
            break

for i in range(1, grid_dim):
    for j in neighbors[grid[i-1][0]]:
        if len(neighbors[j]) < 4 and j in available:
            grid[i][0] = j
            available.remove(j)
            break
    for j in neighbors[grid[i-1][-1]]:
        if len(neighbors[j]) < 4 and j in available:
            grid[i][-1] = j
            available.remove(j)
            break

for i in range(1, grid_dim-1):
    for j in neighbors[grid[-1][i-1]]:
        if len(neighbors[j]) < 4 and j in available:
            grid[-1][i] = j
            available.remove(j)
            break

for i in range(1, grid_dim-1):
    for j in range(1, grid_dim-1):
        for k in neighbors[grid[i-1][j]] & neighbors[grid[i][j-1]]:
            if k in available:
                grid[i][j] = k
                available.remove(k)

str_grid = [[layout[grid[j][i]] for i in range(grid_dim)] for j in range(grid_dim)]

p = list(set(edges[grid[0][0]]) & set(edges[grid[0][1]]))
index = edges[grid[0][0]].index(p[0])
str_grid[0][0] = rotate_string_square_cw(str_grid[0][0], dim, (index+2)%4)
if edges[grid[0][0]][(index+3)%4] not in edges[grid[0][1]]:
    str_grid[0][0] = mirror_string_square(str_grid[0][0], dim)

for i in range(1, grid_dim):
    p = 0
    for j in range(dim):
        p += int(str_grid[i-1][0][j][-1] == "#") << j
    index = edges[grid[i][0]].index(p)
    str_grid[i][0] = rotate_string_square_cw(str_grid[i][0], dim, (index+3)%4)
    if index > 3:
        str_grid[i][0] = mirror_string_square(str_grid[i][0], dim)
        str_grid[i][0] = rotate_string_square_cw(str_grid[i][0], dim, 2)

for i in range(grid_dim):
    for j in range(1, grid_dim):
        p = int(str_grid[i][j-1][-1].replace("#", "1").replace(".", "0"), 2)
        index = edges[grid[i][j]].index(p)
        str_grid[i][j] = rotate_string_square_cw(str_grid[i][j], dim, (index)%4)
        if index > 3:
            str_grid[i][j] = mirror_string_square(str_grid[i][j], dim)

picture = []
picture_dim = grid_dim*(dim-2)
for i in range(grid_dim):
    for j in range(dim):
        if j == 0 or j == dim-1:
            continue
        s = ""
        for k in range(grid_dim):
            s += str_grid[k][i][j][1:dim-1]
        picture.append(s.replace("#", "M"))

print("\n".join(picture))

c = 0
for i in range(8):
    if i > 0:
        picture = rotate_string_square_cw(picture, picture_dim, 1)
    if i == 4:
        picture = mirror_string_square(picture, picture_dim)

    for j in range(picture_dim+1-20):
        for k in range(picture_dim-3):
            if len(re.findall("..................M.", picture[k][j:j+20])) == 1:
                if len(re.findall("M....MM....MM....MMM", picture[k+1][j:j+20])) == 1:
                    if len(re.findall(".M..M..M..M..M..M...", picture[k+2][j:j+20])) == 1:
                        c += 1

print(sum(sum(1 for i in j if i == "M") for j in picture) - 15*c)