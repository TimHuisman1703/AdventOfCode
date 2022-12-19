file = open("aoc13_input.txt")
l = file.read().split("\n")
file.close()

c = []
s = 0
for i in range(len(l)):
    if l[i] == "":
        s = i + 1
        break
    
    a, b = [int(j) for j in l[i].split(",")]
    c += [(a, b)]

instr = l[s].split()[2]
hori = instr[0] == "x"
val = int(instr[2:])

if hori:
    c = [(-abs(j[0] - val) + val, j[1]) for j in c]
else:
    c = [(j[0], -abs(j[1] - val) + val) for j in c]

print(len(set(c)))