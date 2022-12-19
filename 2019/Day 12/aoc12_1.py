file = open("aoc12_input.txt")
l = file.read().split("\n")
file.close()

STEPS = 1000

pos = []
for i in l:
    x, y, z = i.split()
    x = int(x[3:-1])
    y = int(y[2:-1])
    z = int(z[2:-1])
    pos.append([x, y, z])

vel = [[0, 0, 0] for _ in range(len(l))]

for _ in range(STEPS):
    for i in range(len(pos)):
        for j in range(len(pos)):
            if i == j:
                continue

            for k in range(3):
                vel[i][k] += int(pos[i][k] < pos[j][k]) - int(pos[i][k] > pos[j][k])
    
    for i in range(len(pos)):
        for k in range(3):
            pos[i][k] += vel[i][k]

s = 0
for i in range(len(pos)):
    s += sum([abs(j) for j in pos[i]]) * sum([abs(j) for j in vel[i]])
print(s)