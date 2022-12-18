file = open("aoc17_input.txt")
s = file.read()
file.close()

N = 1000000000000

g = [[int(jy == 0 or jx in [0, 8]) for jx in range(9)] for jy in range(10000)]

rocks = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (0, 1), (1, 1)],
]

my = 0
extra = 0
i = j = 0

last_seen = {}

while i < N:
    curr = [(jx + 3, jy + my + 4) for jx, jy in rocks[i % 5]]

    key = (i % 5, j)
    if key in last_seen:
        pi, pmy = last_seen[key]
        di = i - pi
        dmy = my - pmy
        n = (N - i) // di
        i += n * di
        extra = n * dmy
        last_seen = {}
    if i > 1000:
        last_seen[key] = (i, my)

    while 1:
        if s[j] == "<":
            new_curr = [(ix - 1, iy) for ix, iy in curr]
            if all(g[jy][jx] == 0 for jx, jy in new_curr):
                curr = new_curr
        else:
            new_curr = [(ix + 1, iy) for ix, iy in curr]
            if all(g[jy][jx] == 0 for jx, jy in new_curr):
                curr = new_curr
        
        j = (j + 1) % len(s)
        
        new_curr = [(ix, iy - 1) for ix, iy in curr]
        if not all(g[jy][jx] == 0 for jx, jy in new_curr):
            my = max(my, max([j[1] for j in curr]))
            for ix, iy in curr:
                g[iy][ix] = 1
            break
        
        curr = new_curr
    
    i += 1

print(my + extra)