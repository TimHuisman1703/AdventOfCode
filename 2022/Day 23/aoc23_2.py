file = open("aoc23_input.txt")
l = file.read().split("\n")
file.close()

p = set()
d = []
for iy in range(len(l)):
    for ix in range(len(l[iy])):
        if l[iy][ix] == "#":
            d.append((ix, iy))
            p.add((ix, iy))

order = [3, 1, 2, 0, 4]

rounds = 0
no_change = 0
while no_change < 4:
    nd = []
    plan = []
    c = {}

    rounds += 1

    for x, y in d:
        s = 0
        for iy in range(y - 1, y + 2):
            for ix in range(x - 1, x + 2):
                if (ix, iy) in p:
                    s += 1

        new_pos = None
        for i in [order, [4]][s == 1]:
            if i == 0 and not p & set([(x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]):
                new_pos = (x + 1, y)
            if i == 1 and not p & set([(x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]):
                new_pos = (x, y + 1)
            if i == 2 and not p & set([(x - 1, y - 1), (x - 1, y), (x - 1, y + 1)]):
                new_pos = (x - 1, y)
            if i == 3 and not p & set([(x - 1, y - 1), (x, y - 1), (x + 1, y - 1)]):
                new_pos = (x, y - 1)
            if i == 4:
                new_pos = (x, y)

            if new_pos:
                plan.append(new_pos)
                c[new_pos] = c.get(new_pos, 0) + 1
                break

    nd = []
    p = set()
    changed = False
    for a, b in zip(d, plan):
        if c[b] == 1:
            nd.append(b)
            p.add(b)
            changed |= a != b
        else:
            nd.append(a)
            p.add(a)
    d = nd

    if changed:
        no_change = 0
    else:
        no_change += 1

    order = order[1:4] + [order[0]] + [order[4]]

print(rounds + 1 - no_change)