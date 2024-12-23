file = open("aoc23_input.txt")
l = file.read().split("\n")
file.close()

neigh = {}
for w in l:
    a, b = sorted(w.split("-"))
    if a not in neigh:
        neigh[a] = set()
    if b not in neigh:
        neigh[b] = set()
    neigh[a].add(b)

r = 0
for a in neigh:
    for b in neigh[a]:
        for c in neigh[a]:
            if c in neigh[b]:
                if a[0] == "t" or b[0] == "t" or c[0] == "t":
                    r += 1

print(r)