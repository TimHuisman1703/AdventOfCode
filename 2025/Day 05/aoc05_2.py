file = open("aoc05_input.txt")
l = file.read()
file.close()

la, _ = l.split("\n\n")

l = []
for i in la.split():
    a, b = [int(j) for j in i.split("-")]
    l.append((a, b))

l = sorted(l)

idx = 0
while idx < len(l) - 1:
    if l[idx][1] + 1 >= l[idx + 1][0]:
        b = max(l[idx][1], l[idx + 1][1])
        l = l[:idx] + [(l[idx][0], b)] + l[idx + 2:]
    else:
        idx += 1

r = 0
for a, b in l:
    r += b + 1 - a

print(r)