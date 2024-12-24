file = open("aoc24_input.txt")
l = file.read().split("\n\n")
file.close()

import random

gates = []
regs = set()
for w in l[1].split("\n"):
    a, op, b, _, c = w.split()
    a, b = sorted([a, b])
    gates.append([a, b, op, c])
    regs.add(c)

def construct(gs):
    forms = {}
    chains = {}
    for c in "xy":
        for i in range(45):
            k = f"{c}{i:02}"
            forms[k] = k
            chains[k] = {k}

    gs = gs[:]
    while gs:
        gs = sorted(gs, key=lambda x: (x[0] in forms) + (x[1] in forms))
        if (gs[-1][0] in forms) + (gs[-1][1] in forms) < 2:
            return None, None

        a, b, op, c = gs.pop()

        if op == "AND":
            forms[c] = f"({forms[a]} & {forms[b]})"
        elif op == "OR":
            forms[c] = f"({forms[a]} | {forms[b]})"
        elif op == "XOR":
            forms[c] = f"({forms[a]} ^ {forms[b]})"
        chains[c] = {c} | chains[a] | chains[b]

    forms = [forms[k] for k in sorted(forms.keys()) if k[0] == "z"]
    chains = [chains[k] for k in sorted(chains.keys()) if k[0] == "z"]

    return forms, chains

def test(gs):
    forms, _ = construct(gs)

    if forms is None:
        return False

    for _ in range(16):
        x = random.randrange(0, 1 << 45)
        y = random.randrange(0, 1 << 45)

        for j in range(45):
            exec(f"x{j:02} = (x >> {j}) & 1")
            exec(f"y{j:02} = (y >> {j}) & 1")

        z = x + y
        for j in range(i + 1):
            if (z >> j) & 1 != eval(forms[j]):
                return False

    return True

swapped = []
for i in range(46):
    print(f"{i=}")

    if not test(gates):
        print("Problem found, searching for swap...")

        _, chains = construct(gates)
        problematic = {k for k in chains[i] if k[0] != "x" and k[0] != "y"}
        for j in range(i):
            problematic -= chains[j]

        found = False
        for x in regs:
            for y in problematic:
                ngs = []
                for a, b, op, c in gates:
                    c = y if c == x else x if c == y else c
                    ngs.append((a, b, op, c))

                if test(ngs):
                    print(f"Swapped {x} and {y}")
                    gates = ngs
                    swapped.extend([x, y])
                    found = True
                    break
            if found:
                break

print(",".join(sorted(swapped)))