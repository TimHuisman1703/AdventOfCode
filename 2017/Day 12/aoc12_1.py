file = open("aoc12_input.txt")
l = file.read().split("\n")
file.close()

conn = {}
for desc in l:
    args = desc.replace(",", "").split()

    conn.update({int(args[0]): [int(j) for j in args[2:]]})

group = [0]
i = 0
while i < len(group):
    for j in conn[group[i]]:
        if j not in group:
            group.append(j)
    i += 1

print(len(group))