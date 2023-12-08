file = open("aoc08_input.txt")
l = file.read().split("\n")
file.close()

from math import lcm

instrs = l[0]
children = {}
for w in l[2:]:
    p, c = w.split(" = ")
    children[p] = c[1:-1].split(", ")

p = 1
nodes = [j for j in children.keys() if j[-1] == "A"]
for node in nodes:
    idx = 0
    while True:
        node = children[node][instrs[idx % len(instrs)] == "R"]
        idx += 1
        if node[-1] == "Z":
            break
    p = lcm(idx, p)

print(p)