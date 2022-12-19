file = open("aoc22_input.txt")
l = file.read().split("\n")
file.close()

nodes = []

for s in l[2:]:
    while "  " in s:
        s = s.replace("  ", " ")
    args = s.split()
    
    _, x, y = args[0].split("-")
    x, y = int(x[1:]), int(y[1:])
    used = int(args[2][:-1])
    available = int(args[3][:-1])

    nodes.append(((x, y), used, available))

c = 0
for i in range(len(nodes)):
    if nodes[i][1] == 0:
        continue
    
    for j in range(len(nodes)):
        if i == j:
            continue
        
        if nodes[i][1] <= nodes[j][2]:
            c += 1

print(c)