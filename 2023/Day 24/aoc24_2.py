file = open("aoc24_input.txt")
l = file.read().split("\n")
file.close()

import sympy as sym

N = 4

vars = sym.symbols("px py pz vx vy vz " + " ".join(f"t{j}" for j in range(N)))
ps = vars[:3]
vs = vars[3:6]
ts = vars[6:]

equations = []
for i, w in enumerate(l[:N]):
    p, v = w.split(" @ ")

    p = [int(j) for j in p.split(", ")]
    v = [int(j) for j in v.split(", ")]

    for c in range(3):
        eq = sym.Eq(p[c] + v[c] * ts[i], ps[c] + vs[c] * ts[i])
        equations.append(eq)

result = sym.solve(equations, vars)[0]

print(sum(result[:3]))