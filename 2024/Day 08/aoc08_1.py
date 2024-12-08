file = open("aoc08_input.txt")
l = file.read().split("\n")
file.close()

d = {}
for iy in range(len(l)):
    for ix in range(len(l[iy])):
        c = l[iy][ix]
        if c != ".":
            if c not in d:
                d[c] = []
            d[c].append((ix, iy))

seen = set()
for c in d:
    dc = d[c]
    for i in range(len(dc)):
        for j in range(i + 1, len(dc)):
            seen.add(tuple(2 * dc[i][k] - dc[j][k] for k in range(2)))
            seen.add(tuple(2 * dc[j][k] - dc[i][k] for k in range(2)))

r = 0
for x, y in seen:
    if x >= 0 and x < len(l[0]) and y >= 0 and y < len(l):
        r += 1

print(r)