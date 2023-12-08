file = open("aoc08_input.txt")
l = file.read().split("\n")
file.close()

instrs = l[0]
children = {}
for w in l[2:]:
    p, c = w.split(" = ")
    children[p] = c[1:-1].split(", ")

node = "AAA"

idx = 0
while node != "ZZZ":
    node = children[node][instrs[idx % len(instrs)] == "R"]
    idx += 1

print(idx)