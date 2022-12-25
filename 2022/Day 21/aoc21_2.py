file = open("aoc21_input.txt")
l = file.read().split("\n")
file.close()

d = {}

for i in l:
    name, *instr = i.split()
    d[name[:-1]] = instr

def f(s, choice):
    if s == "humn":
        return choice
    
    if len(d[s]) == 1:
        return int(d[s][0])
    
    a, op, b = d[s]
    return eval(f"{f(a, choice)} {op} {f(b, choice)}")

node_a, _, node_b = d["root"]
if f(node_a, 0) == f(node_a, 1):
    node_a, node_b = node_b, node_a

goal = f(node_b, 0)

a = 0
b = 1
while f(node_a, b) > goal:
    b *= 2

while a != b:
    mid = (a + b + 1) // 2
    value = f(node_a, mid)
    if f(node_a, mid) < goal:
        b = mid - 1
    else:
        a = mid

print(a)