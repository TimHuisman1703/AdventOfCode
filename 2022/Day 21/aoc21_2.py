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

A = "ddzt"
B = "rmtp"

goal = f(B, 0)

a = 0
b = 1
while f(A, b) > goal:
    b *= 2

while a != b:
    mid = (a + b + 1) // 2
    value = f(A, mid)
    if f(A, mid) < goal:
        b = mid - 1
    else:
        a = mid

print(a)