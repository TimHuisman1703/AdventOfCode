file = open("aoc17_input.txt")
l = file.read().split("\n")
file.close()

a, b, c = [int(l[j].split()[-1]) for j in range(3)]
instrs = [int(j) for j in l[-1].split()[-1].split(",")]

def combo(i):
    if i < 4:
        return i
    else:
        return [a, b, c][i - 4]

idx = 0
output = []
while idx < len(instrs) - 1:
    cmd = instrs[idx]
    ope = instrs[idx + 1]
    if cmd == 0:
        a = a >> combo(ope)
    elif cmd == 1:
        b ^= ope
    elif cmd == 2:
        b = combo(ope) % 8
    elif cmd == 3:
        if a:
            idx = ope
            continue
    elif cmd == 4:
        b = b ^ c
    elif cmd == 5:
        output.append(combo(ope) % 8)
    elif cmd == 6:
        b = a >> combo(ope)
    elif cmd == 7:
        c = a >> combo(ope)
    idx += 2

print(",".join(str(j) for j in output))