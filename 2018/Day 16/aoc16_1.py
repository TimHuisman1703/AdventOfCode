file = open("aoc16_input.txt")
l = file.read().split("\n")
file.close()

def execute(op, a, b, c, r):
    if op == "addr":
        r[c] = r[a] + r[b]
    elif op == "addi":
        r[c] = r[a] + b
    elif op == "mulr":
        r[c] = r[a] * r[b]
    elif op == "muli":
        r[c] = r[a] * b
    elif op == "banr":
        r[c] = r[a] & r[b]
    elif op == "bani":
        r[c] = r[a] & b
    elif op == "borr":
        r[c] = r[a] | r[b]
    elif op == "bori":
        r[c] = r[a] | b
    elif op == "setr":
        r[c] = r[a]
    elif op == "seti":
        r[c] = a
    elif op == "gtir":
        r[c] = int(a > r[b])
    elif op == "gtri":
        r[c] = int(r[a] > b)
    elif op == "gtrr":
        r[c] = int(r[a] > r[b])
    elif op == "eqir":
        r[c] = int(a == r[b])
    elif op == "eqri":
        r[c] = int(r[a] == b)
    elif op == "eqrr":
        r[c] = int(r[a] == r[b])
    
    return r

opcodes = "addr addi mulr muli banr bani borr bori setr seti gtir gtri gtrr eqir eqri eqrr".split()

s = 0

i = 0
while l[i]:
    before = eval(l[i][8:])
    after = eval(l[i+2][7:])
    _, a, b, c = [int(j) for j in l[i+1].split()]

    possible = 0
    for op in opcodes:
        if execute(op, a, b, c, before[:]) == after:
            possible += 1
    
    if possible >= 3:
        s += 1

    i += 4

print(s)