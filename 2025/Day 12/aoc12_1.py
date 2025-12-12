file = open("aoc12_input.txt")
l = file.read()
file.close()

l = l.split("\n\n")
ps = l[:-1]
ps = [[[int(c == "#") for c in row] for row in p.split("\n")[1:]] for p in ps]

sizes = [sum(sum(row) for row in p) for p in ps]

r = 0
for row in l[-1].split("\n"):
    wh, *qs = row.split()
    w, h = [int(j) for j in wh[:-1].split("x")]

    qs = [int(j) for j in qs]

    if sum(sizes[j] * qs[j] for j in range(len(ps))) <= w * h:
        r += 1

print(r)