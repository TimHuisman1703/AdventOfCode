file = open("aoc15_input.txt")
l = file.read().split("\n")
file.close()

positions = []
offset = []

for statement in l:
    args = statement.split()
    positions.append(int(args[3]))
    offset.append(int(args[11][:-1]))

positions.append(11)
offset.append(0)

for i in range(len(offset)):
    offset[i] = (offset[i] + (i+1)) % positions[i]

k = 1
t = 0
for i in range(len(offset)):
    while t % positions[i] != -offset[i] % positions[i]:
        t += k
    
    k *= positions[i]

print(t)