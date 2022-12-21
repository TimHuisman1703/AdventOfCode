file = open("aoc21_input.txt")
l = file.read().split("\n")
file.close()

d = {}

for i in l:
    name, *instr = i.split()
    d[name[:-1]] = instr

def f(s):
    if len(d[s]) == 1:
        return int(d[s][0])
    
    a, op, b = d[s]
    return eval(f"{f(a)} {op.replace('/', '//')} {f(b)}")

print(f("root"))