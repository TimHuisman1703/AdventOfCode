file = open("aoc24_input.txt")
l = file.read().split("\n\n")
file.close()

reg = {}
for w in l[0].split("\n"):
    k, v = w.split(": ")
    reg[k] = int(v)

gates = []
for w in l[1].split("\n"):
    a, op, b, _, c = w.split()
    gates.append([a, b, op, c])

while gates:
    gates = sorted(gates, key=lambda x: (x[0] in reg) + (x[1] in reg))
    a, b, op, c = gates.pop()

    if op == "AND":
        reg[c] = reg[a] & reg[b]
    elif op == "OR":
        reg[c] = reg[a] | reg[b]
    elif op == "XOR":
        reg[c] = reg[a] ^ reg[b]

r = "".join(str(reg[j]) for j in sorted(reg.keys())[::-1] if j[0] == "z")
print(int(r, 2))