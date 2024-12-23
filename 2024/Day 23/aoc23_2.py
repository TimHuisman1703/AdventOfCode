file = open("aoc23_input.txt")
l = file.read().split("\n")
file.close()

neigh = {}
for w in l:
    a, b = w.split("-")
    if a not in neigh:
        neigh[a] = set()
    if b not in neigh:
        neigh[b] = set()
    neigh[a].add(b)
    neigh[b].add(a)

cl = [{key} for key in neigh.keys()]
while True:
    print(f"len(cl) = {len(cl)}")
    ncl = []

    for c in cl:
        for n in neigh.keys():
            for x in c:
                if n not in neigh[x]:
                    break
                if n < x:
                    break
            else:
                ncl.append(c | {n})

    if not ncl:
        break
    cl = ncl

print(*sorted(cl[0]), sep=",")