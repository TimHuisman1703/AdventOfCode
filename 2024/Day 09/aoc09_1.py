file = open("aoc09_input.txt")
l = file.read().split("\n")
file.close()

r = []
idx = 1
for c in l[0]:
    c = int(c)
    r.extend(c * [max(0, idx)])

    if idx > 0:
        idx = -idx
    else:
        idx = -idx + 1

idx = 0
while idx < len(r):
    if r[idx] == 0:
        if r[-1] == 0:
            r.pop()
        else:
            r[idx] = r.pop()
            idx += 1
    else:
        idx += 1

s = 0
for i, c in enumerate(r):
    if r[i]:
        s += i * (c - 1)

print(s)