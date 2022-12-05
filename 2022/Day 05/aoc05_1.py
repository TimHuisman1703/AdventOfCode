file = open("aoc05_input.txt")
l = file.read().split("\n")
file.close()

b = []

i = 0
while l[i][1] != "1":
    while 4 * len(b) < len(l[i]):
        b.append([])
    for j in range(1, len(l[i]), 4):
        if l[i][j] != " ":
            b[j // 4].append(l[i][j])
    i += 1

b = [j[::-1] for j in b]

i += 2

while i < len(l):
    _, p, _, q, _, r = l[i].split()
    p, q, r = [int(j) for j in [p, q, r]]

    for j in range(p):
        b[r - 1].append(b[q - 1].pop())

    i += 1

print("".join(j[-1] for j in b))